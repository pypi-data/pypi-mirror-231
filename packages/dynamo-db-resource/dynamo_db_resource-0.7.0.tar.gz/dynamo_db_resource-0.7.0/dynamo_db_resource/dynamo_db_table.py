from aws_schema import SchemaValidator
from aws_schema.nested_dict_helper import find_path_values_in_dict
from ._number_types_in_objects import (
    object_with_float_to_decimal,
    object_with_decimal_to_float,
)
from ._schema import DynamoDBValidator
from .exceptions import (
    ConditionalCheckFailedException,
    AttributeExistsException,
    AttributeNotExistsException,
    ValidationError,
    CustomExceptionRaiser,
)
from inspect import stack
from os import environ as os_environ
from string import ascii_lowercase
from boto3 import resource
from boto3.dynamodb.conditions import (
    Key,
    And,
    ConditionExpressionBuilder,
    ConditionBase,
)
from botocore.exceptions import ClientError
from copy import deepcopy
from typing import Iterable, List

_ddb_resource = resource(
    "dynamodb",
    **{
        "region_name": os_environ["AWS_REGION"]
        if "AWS_REGION" in os_environ
        else "us-east-1"
    },
)

__all__ = ["Table", "UpdateReturns", "SelectReturns"]


class UpdateReturns:
    """
    contains the options for possible return values if updating an item
    """

    NONE = "NONE"
    ALL_OLD = "ALL_OLD"
    UPDATED_OLD = "UPDATED_OLD"
    ALL_NEW = "ALL_NEW"
    UPDATED_NEW = "UPDATED_NEW"
    DELETED = "UPDATED_OLD"


class SelectReturns:
    """
    contains the options for query return values
    """

    ALL_ATTRIBUTES = "ALL_ATTRIBUTES"
    ALL_PROJECTED_ATTRIBUTES = "ALL_PROJECTED_ATTRIBUTES"
    SPECIFIC_ATTRIBUTES = "SPECIFIC_ATTRIBUTES"
    COUNT = "COUNT"


_value_update_chars = list()
for c1 in ascii_lowercase:
    for c2 in ascii_lowercase:
        _value_update_chars.append(c1 + c2)


def _cast_table_name(table_name: str, config: dict = None) -> str:
    name_components = list()
    if config and "stage" in config:
        name_components.append(config["stage"])
    elif "DYNAMO_DB_RESOURCE_STAGE_NAME" in os_environ:
        name_components.append(os_environ["DYNAMO_DB_RESOURCE_STAGE_NAME"])
    if config and "stack" in config:
        name_components.append(config["stack"])
    elif "DYNAMO_DB_RESOURCE_STACK_NAME" in os_environ:
        name_components.append(os_environ["DYNAMO_DB_RESOURCE_STACK_NAME"])
    name_components.append(table_name)
    return "-".join(name_components)


def _combine_and_conditions(conditions: list):
    if len(conditions) == 1:
        con = conditions[0]

    else:
        con = And(*conditions)
    return ConditionExpressionBuilder().build_expression(con)


class Table:
    def __init__(
        self, table_name, special_resource_config: dict = False, config: dict = None
    ):
        self.__table_name = table_name
        self._config = config if config else {}
        self.__custom_exception_raiser = CustomExceptionRaiser(self)

        origin = (
            self._config["origin"].lower()
            if "origin" in self._config
            else os_environ["DYNAMO_DB_RESOURCE_SCHEMA_ORIGIN"].lower()
        )
        directory = (
            self._config["directory"]
            if "directory" in self._config
            else os_environ["DYNAMO_DB_RESOURCE_SCHEMA_DIRECTORY"]
        )
        directory += self.__table_name
        self.__schema_validator = SchemaValidator(
            **{origin: directory}, custom_validator=DynamoDBValidator
        )

        if special_resource_config:
            self.__resource = resource("dynamodb", **special_resource_config)
            self.__resource_config = special_resource_config
        else:
            self.__resource = _ddb_resource
            self.__resource_config = {"region_name": os_environ["AWS_REGION"]}
        self.__table_name = _cast_table_name(table_name, self._config)
        self.__table = self.__resource.Table(self.__table_name)
        self._cast_indexes()

    @property
    def name(self):
        return self.__table_name

    @property
    def pk(self):
        return tuple(
            [
                i["AttributeName"]
                for i in self.__schema_validator.schema["$infrastructure"]["KeySchema"]
            ]
        )

    @property
    def schema(self):
        return self.__schema_validator.schema

    @property
    def table(self):
        return self.__table

    @property
    def indexes(self) -> dict:
        return self.__indexes

    @property
    def custom_exception(self):
        return self.__custom_exception_raiser

    def _cast_indexes(self):
        self.__indexes = dict()
        for k in ["LocalSecondaryIndexes", "GlobalSecondaryIndexes"]:
            self.__indexes.update(
                {
                    indexes["IndexName"]: tuple(
                        [i["AttributeName"] for i in indexes["KeySchema"]]
                    )
                    for indexes in self.schema["$infrastructure"].get(k, list())
                }
            )

    @property
    def _item_not_exists_condition(self):
        return " and ".join([f"attribute_not_exists({pk})" for pk in self.pk])

    @property
    def _item_exists_condition(self):
        return " and ".join([f"attribute_exists({pk})" for pk in self.pk])

    @staticmethod
    def _attribute_not_exists_condition(paths_to_attributes):
        return " and ".join(
            [f"attribute_not_exists({'.'.join(path)})" for path in paths_to_attributes]
        )

    @staticmethod
    def _attribute_exists_condition(paths_to_attributes):
        return " and ".join(
            [f"attribute_exists({'.'.join(path)})" for path in paths_to_attributes]
        )

    def _cast_primary_keys(self, *primary_data, batch=False):
        if not batch:
            if len(primary_data) == 2 and not isinstance(primary_data, str):
                return {self.pk[i]: primary_data[i] for i in range(2)}
            if isinstance(primary_data[0], dict):
                return primary_data[0]
            if isinstance(primary_data[0], str):
                return {self.pk[0]: primary_data[0]}
        casted_keys = list()
        for item in primary_data:
            for i in item:
                if isinstance(i, dict):
                    casted_keys.append(i)
                elif isinstance(i, str):
                    casted_keys.append({self.pk[0]: i})
                elif isinstance(i, Iterable):
                    casted_keys.append(dict(zip(self.pk, i)))
        return casted_keys

    def _validate_input(self, given_input):
        function_name = stack()[1].function
        if any([i in function_name for i in ["update", "add"]]):
            try:
                self.__schema_validator.validate_sub_part(given_input)
            except ValidationError as e:
                self.custom_exception.wrong_data_type(e)

        elif "put" == function_name:
            try:
                self.__schema_validator.validate(given_input)
            except ValidationError as e:
                self.custom_exception.wrong_data_type(e)

        elif "remove_attribute" == function_name:
            for path in given_input:
                path_to_attribute = path[:-1]
                attribute = path[-1]
                sub_schema, _ = self.__schema_validator.get_sub_schema(
                    path_to_attribute
                )
                if attribute in sub_schema.get("required", list()):
                    self.custom_exception.removing_required_attribute(
                        attribute, path_to_attribute
                    )
        else:
            self._primary_key_checker(given_input)

    def _primary_key_checker(self, given_primaries):
        if not all(pk in given_primaries for pk in self.pk):
            self.custom_exception.missing_primary_key(
                tuple([key for key in self.pk if key not in given_primaries])
            )
        elif len(given_primaries) > len(self.pk):
            self.custom_exception.wrong_primary_key(given_primaries)

    def _cast_index_keys(self, index: str, *index_primary_data) -> dict:
        if isinstance(index_primary_data[0], dict):
            return index_primary_data[0]
        return {
            self.indexes[index][i]: index_primary_data[i]
            for i in range(len(index_primary_data))
        }

    def _index_key_checker(self, index: str, index_primary: dict):
        if not all(ik in index_primary for ik in self.indexes[index]):
            self.custom_exception.missing_primary_key(
                tuple([key for key in self.indexes[index] if key not in index_primary])
            )
        elif len(index_primary) > len(self.indexes[index]):
            self.custom_exception.wrong_primary_key(index_primary)

    def _create_projection_expression(
        self, attributes_to_get, existing_data: dict = None
    ):
        if existing_data is None:
            existing_data = dict()

        letter_count = 0
        attribute_expression_map = dict()
        attribute_expressions = list()

        def next_expression(attribute_name, lc):
            if (
                attribute_name
                in existing_data.get("ExpressionAttributeNames", dict()).values()
            ):
                return {
                    va: k
                    for k, va in existing_data.get(
                        "ExpressionAttributeNames", dict()
                    ).items()
                }[attribute_name], lc
            letter = f"#{_value_update_chars[lc].upper()}"
            attribute_expression_map[letter] = attribute_name
            lc += 1
            return letter, lc

        if isinstance(attributes_to_get, str):
            attributes_to_get = [attributes_to_get]
        for i in self.pk:
            if i not in attributes_to_get:
                attributes_to_get.append(i)
        for i, v in enumerate(attributes_to_get):
            if isinstance(v, list):
                nested_attribute = list()
                for vi, value in enumerate(v):
                    if isinstance(value, int):
                        nested_attribute.append(f"[{value}]")
                    else:
                        l, letter_count = next_expression(value, letter_count)
                        nested_attribute.append(l)
                attribute_expressions.append(".".join(nested_attribute))
            else:
                l, letter_count = next_expression(v, letter_count)
                attribute_expressions.append(l)
        return ",".join(attribute_expressions), attribute_expression_map

    def describe(self):
        from boto3 import client

        dynamo_db_client = client("dynamodb", **self.__resource_config)
        response = dynamo_db_client.describe_table(TableName=self.__table_name)
        return response

    def get(self, attributes_to_get: list = None, **primary_dict):
        """
        get item specified with primary_dict

        Parameters
        ----------
        attributes_to_get: list, optional
            specify certain attributes to get
        primary_dict: str
            primary keys for the item to retrieve

        Returns
        -------
        dict

        """
        self._primary_key_checker(primary_dict)

        get_data = {"Key": primary_dict}
        if attributes_to_get:
            expression, name_map = self._create_projection_expression(attributes_to_get)
            get_data.update(
                {
                    "ProjectionExpression": expression,
                    "ExpressionAttributeNames": name_map,
                }
            )

        response = self.__table.get_item(**get_data)

        if "Item" not in response:
            self.custom_exception.not_found_message(primary_dict)
        else:
            try:
                return object_with_decimal_to_float(response["Item"])
            except KeyError:
                return [
                    object_with_decimal_to_float(item) for item in response["Items"]
                ]

    @staticmethod
    def _create_remove_expression(
        path_to_attribute: list,
        list_position_if_list: int = None,
        set_items_if_set: list = None,
    ):

        expression = "remove " if not set_items_if_set else "delete "
        attribute_key_mapping = dict()
        expression_values = dict()
        letter_count = 0

        def assign_key_to_attribute_path_step(attribute_name, letter_count):
            if attribute_name not in attribute_key_mapping:
                attribute_key_mapping[
                    attribute_name
                ] = f"#{_value_update_chars[letter_count].upper()}"
                letter_count += 1
            return letter_count

        for path_no, path in enumerate(path_to_attribute):
            for attribute in path:
                letter_count = assign_key_to_attribute_path_step(
                    attribute, letter_count
                )
                expression += f"{attribute_key_mapping[attribute]}."
            expression = expression[:-1]
            if set_items_if_set is not None:
                expression += f" :{_value_update_chars[path_no]}"
                expression_values[
                    f":{_value_update_chars[path_no]}"
                ] = object_with_float_to_decimal(set_items_if_set[path_no])
            expression += ", "

        expression = expression[:-2]

        if list_position_if_list is not None:
            expression += f"[{list_position_if_list}]"

        return (
            expression,
            expression_values,
            {v: k for k, v in attribute_key_mapping.items()},
        )

    @staticmethod
    def _create_update_expression(
        new_data: dict = None,
        *,
        paths_to_new_data=None,
        values_per_path=None,
        list_operation: (bool, list, tuple) = False,
        set_operation: (bool, set) = False,
        value_operation: bool = False,
    ):
        expression = "set " if (value_operation or not set_operation) else "add "
        expression_values = dict()

        if not paths_to_new_data or not values_per_path:
            paths_to_new_data, values_per_path = find_path_values_in_dict(
                deepcopy(new_data)
            )

        if isinstance(list_operation, bool):
            list_operation = [list_operation for i in paths_to_new_data]
        if isinstance(set_operation, bool):
            set_operation = [set_operation for i in paths_to_new_data]
        if isinstance(value_operation, bool):
            value_operation = [value_operation for i in paths_to_new_data]

        attribute_key_mapping = dict()
        letters_used = 0

        def update_expression_attribute():
            if list_operation[path_no]:
                return f"= list_append({string_path_to_attribute}, :{_value_update_chars[path_no]})"
            if set_operation[path_no]:
                return f":{_value_update_chars[path_no]}"
            if value_operation[path_no]:
                return f"= {string_path_to_attribute} + :{_value_update_chars[path_no]}"
            return f"= :{_value_update_chars[path_no]}"

        def update_expression_value():
            expression_values[
                f":{_value_update_chars[path_no]}"
            ] = object_with_float_to_decimal(values_per_path[path_no])

        def assign_key_to_attribute_path_step(attribute_name, letter_count):
            if attribute_name not in attribute_key_mapping:
                attribute_key_mapping[
                    attribute_name
                ] = f"#{_value_update_chars[letter_count].upper()}"
                letter_count += 1
            return letter_count

        def create_path_to_attribute_with_mapped_keys(
            left_path_to_process, path_with_keys, letter_count
        ):
            for step in left_path_to_process:
                letter_count = assign_key_to_attribute_path_step(step, letter_count)

                path_with_keys.append(attribute_key_mapping[step])

            return path_with_keys, letter_count

        for path_no in range(len(paths_to_new_data)):
            path = paths_to_new_data[path_no]

            path_with_letter_keys = list()

            (
                path_with_letter_keys,
                letters_used,
            ) = create_path_to_attribute_with_mapped_keys(
                path, path_with_letter_keys, letters_used
            )

            string_path_to_attribute = ".".join(path_with_letter_keys)

            expression += (
                f"{string_path_to_attribute} {update_expression_attribute()}, "
            )

            update_expression_value()

        return (
            expression[:-2],
            expression_values,
            {v: k for k, v in attribute_key_mapping.items()},
            paths_to_new_data,
        )

    def _build_conditions(
        self,
        existing_attribute_paths: (list, None),
        not_existing_attribute_paths: (list, None),
        expression_name_map: dict,
        direct_conditions=None,
    ):

        if not any(
            [existing_attribute_paths, not_existing_attribute_paths, direct_conditions]
        ):
            return None

        conditions = list()
        att_map = dict()
        val_map = dict()

        expression_name_map = {v: k for k, v in expression_name_map.items()}

        if existing_attribute_paths:
            existing_attribute_paths = [
                [expression_name_map[path[pos]] for pos in range(len(path))]
                for path in existing_attribute_paths
            ]

            conditions.append(
                self._attribute_exists_condition(existing_attribute_paths)
            )

        if not_existing_attribute_paths:
            not_existing_attribute_paths = [
                [expression_name_map[path[pos]] for pos in range(len(path))]
                for path in not_existing_attribute_paths
            ]
            conditions.append(
                self._attribute_not_exists_condition(not_existing_attribute_paths)
            )
        if direct_conditions:
            if not isinstance(direct_conditions, Iterable):
                cond, att_map, val_map = ConditionExpressionBuilder().build_expression(
                    direct_conditions
                )
            else:
                cond, att_map, val_map = ConditionExpressionBuilder().build_expression(
                    And(*direct_conditions)
                )
            conditions.append(cond)

        return " and ".join(conditions), att_map, val_map

    def __general_update(
        self,
        *,
        require_attributes_already_present=False,
        require_attributes_to_be_missing=False,
        create_item_if_non_existent,
        list_operation=False,
        set_operation=False,
        value_operation=False,
        returns: UpdateReturns = UpdateReturns.NONE,
        new_data=None,
        remove_data=None,
        remove_set_item=None,
        remove_list_item=None,
        direct_condition=None,
        **primary_dict,
    ):
        self._primary_key_checker(primary_dict)

        if new_data:
            self._validate_input(new_data)
            # ToDo create condition for attribute still required length if schema contains maxItems/maxProperties
            (
                update_expression,
                expression_value_map,
                expression_name_map,
                paths_to_data,
            ) = self._create_update_expression(
                new_data,
                list_operation=list_operation,
                set_operation=set_operation,
                value_operation=value_operation,
            )

        else:
            # ToDo create condition for attribute still required length if schema contains minItems/minProperties
            (
                update_expression,
                expression_value_map,
                expression_name_map,
            ) = self._create_remove_expression(
                remove_data, remove_list_item, remove_set_item
            )
            paths_to_data = remove_data.copy()

        necessary_attribute_paths = list()
        if require_attributes_already_present:
            necessary_attribute_paths = paths_to_data
        if not create_item_if_non_existent:
            for k in self.pk:
                _expression_name_key = _value_update_chars[len(expression_name_map)]
                expression_name_map[f"#{_expression_name_key.upper()}"] = k
                necessary_attribute_paths.append([k])

        if condition_data := self._build_conditions(
            existing_attribute_paths=necessary_attribute_paths,
            not_existing_attribute_paths=paths_to_data
            if require_attributes_to_be_missing
            else None,
            expression_name_map=expression_name_map,
            direct_conditions=direct_condition,
        ):
            condition_expression = condition_data[0]
            expression_name_map.update(condition_data[1])
            expression_value_map.update(condition_data[2])
        else:
            condition_expression = str()

        update_dict = {
            "Key": primary_dict,
            "UpdateExpression": update_expression,
            "ExpressionAttributeNames": expression_name_map,
            "ExpressionAttributeValues": expression_value_map,
            "ReturnValues": returns,
            "ConditionExpression": condition_expression,
        }
        for key, value in update_dict.copy().items():
            if not value:
                update_dict.pop(key)

        def return_only_deleted(resp):
            return_data = [resp for _ in remove_data]
            for index, rd in enumerate(return_data):
                while remove_data[index]:
                    rd = rd[remove_data[index].pop(0)]
                    try:
                        return_data[index] = (
                            rd[remove_list_item] if remove_list_item else rd
                        )
                    except KeyError:
                        raise IndexError("the given position_to_delete does not exist")
                resp = return_data
            if len(remove_data) == 1:
                [resp] = resp
            return resp

        def handle_response(resp):
            if "Attributes" in resp:
                resp = object_with_decimal_to_float(resp["Attributes"])
                if returns == UpdateReturns.DELETED and remove_data:
                    resp = return_only_deleted(resp)
                return resp

        try:
            response = self.__table.update_item(**update_dict)
            return handle_response(response)
        except ClientError as CE:
            if CE.response["Error"]["Code"] == "ValidationException":
                if "document path provided in the update expression is invalid for update" in CE.response[
                    "Error"
                ][
                    "Message"
                ] or (
                    "provided expression refers to an attribute that does not exist in the item"
                    in CE.response["Error"]["Message"]
                    and not require_attributes_already_present
                ):
                    from aws_schema.nested_dict_helper import find_new_paths_in_dict

                    try:
                        item = self.get(**primary_dict)
                        path_dict, new_sub_dict = find_new_paths_in_dict(item, new_data)
                        (
                            expression,
                            values,
                            expression_name_map,
                            _,
                        ) = self._create_update_expression(
                            paths_to_new_data=path_dict, values_per_path=new_sub_dict
                        )
                        update_dict = {
                            "Key": primary_dict,
                            "UpdateExpression": expression,
                            "ExpressionAttributeValues": values,
                            "ExpressionAttributeNames": expression_name_map,
                            "ReturnValues": returns,
                        }
                        response = self.__table.update_item(**update_dict)
                        return handle_response(response)
                    except FileNotFoundError as FNF:
                        if create_item_if_non_existent:
                            item = primary_dict.copy()
                            item.update(new_data)
                            self.put(item)
                        else:
                            raise FNF

            elif CE.response["Error"]["Code"] == "ConditionalCheckFailedException":
                try:
                    # ToDo check for min/max Items/Properties once condition based on schema implemented
                    if direct_condition:
                        raise ConditionalCheckFailedException
                    self.get(**primary_dict)
                    if require_attributes_already_present:
                        raise AttributeNotExistsException
                    else:
                        raise AttributeExistsException
                except FileNotFoundError as FNF:
                    if create_item_if_non_existent:
                        item = primary_dict.copy()
                        item.update(new_data)
                        self.put(item)
                    else:
                        raise FNF
            else:
                raise CE
        # except AssertionError as AE:
        #     try:
        #         item = self.get(**primary_dict)
        #         if require_attributes_already_present:
        #             raise AttributeNotExistsException
        #         else:
        #             raise AttributeExistsException
        #     except FileNotFoundError as FNF:
        #         if create_item_if_non_existent:
        #             item = primary_dict.copy()
        #             item.update(new_data)
        #             self.put(item)
        #         else:
        #             raise FNF
        #     raise AE

    # https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html
    def add_new_attribute(
        self,
        new_data: dict,
        update_if_existent=False,
        create_item_if_non_existent=False,
        returns: UpdateReturns = UpdateReturns.NONE,
        condition=None,
        **primary_dict,
    ):
        self._validate_input(new_data)
        return self.__general_update(
            **primary_dict,
            new_data=new_data,
            require_attributes_to_be_missing=True if not update_if_existent else False,
            create_item_if_non_existent=create_item_if_non_existent,
            direct_condition=condition,
            returns=returns,
        )

    def update_attribute(
        self,
        new_data,
        set_new_attribute_if_not_existent=False,
        create_item_if_non_existent=False,
        returns: UpdateReturns = UpdateReturns.NONE,
        condition=None,
        **primary_dict,
    ):
        return self.__general_update(
            **primary_dict,
            new_data=new_data,
            require_attributes_already_present=True
            if not set_new_attribute_if_not_existent
            else False,
            create_item_if_non_existent=create_item_if_non_existent,
            direct_condition=condition,
            returns=returns,
        )

    def update_list_item(self, primary_dict, item_no, condition=None, **new_data):
        raise NotImplemented

    def update_append_list(
        self,
        new_data,
        set_new_attribute_if_not_existent=False,
        create_item_if_non_existent=False,
        returns: UpdateReturns = UpdateReturns.NONE,
        condition=None,
        **primary_dict,
    ):
        return self.__general_update(
            **primary_dict,
            new_data=new_data,
            require_attributes_already_present=False
            if set_new_attribute_if_not_existent
            else True,
            create_item_if_non_existent=create_item_if_non_existent,
            list_operation=True,
            direct_condition=condition,
            returns=returns,
        )

    def update_add_set(
        self,
        new_data: dict,
        set_new_attribute_if_not_existent=False,
        create_item_if_non_existent=False,
        returns: UpdateReturns = UpdateReturns.NONE,
        condition=None,
        **primary_dict,
    ):
        return self.__general_update(
            **primary_dict,
            new_data=new_data,
            require_attributes_already_present=False
            if set_new_attribute_if_not_existent
            else True,
            create_item_if_non_existent=create_item_if_non_existent,
            set_operation=True,
            direct_condition=condition,
            returns=returns,
        )

    def update_number_drift(
        self,
        drift_values_in_dict: dict,
        set_new_attribute_if_not_existent=False,
        create_item_if_non_existent=False,
        returns: UpdateReturns = UpdateReturns.NONE,
        condition=None,
        **primary_dict,
    ):
        return self.__general_update(
            **primary_dict,
            new_data=drift_values_in_dict,
            require_attributes_already_present=False
            if set_new_attribute_if_not_existent
            else True,
            create_item_if_non_existent=create_item_if_non_existent,
            value_operation=True,
            direct_condition=condition,
            returns=returns,
        )

    def put(self, item, overwrite=False):
        self._validate_input(item)

        try:
            item_copy = deepcopy(item)
            self.__table.put_item(
                Item=object_with_float_to_decimal(item_copy),
                ConditionExpression=self._item_not_exists_condition,
            ) if not overwrite else self.__table.put_item(
                Item=object_with_float_to_decimal(item_copy)
            )

        except ClientError as CE:
            if CE.response["Error"]["Code"] == "ConditionalCheckFailedException":
                self.custom_exception.item_already_existing(item)
            else:
                raise CE

    def remove_attribute(
        self,
        path_of_attribute: list,
        returns: UpdateReturns = UpdateReturns.NONE,
        condition=None,
        **primary_dict,
    ):
        if not isinstance(path_of_attribute[0], list):
            path_of_attribute = [path_of_attribute]
        self._validate_input(path_of_attribute)
        return self.__general_update(
            require_attributes_already_present=True,
            create_item_if_non_existent=False,
            remove_data=path_of_attribute.copy(),
            returns=returns,
            direct_condition=condition,
            **primary_dict,
        )

    def remove_entry_in_list(
        self,
        path_to_list: list,
        position_to_delete: int,
        returns: UpdateReturns = UpdateReturns.NONE,
        condition=None,
        **primary_dict,
    ):
        if not isinstance(path_to_list[0], list):
            path_to_list = [path_to_list]
        return self.__general_update(
            require_attributes_already_present=True,
            create_item_if_non_existent=False,
            remove_data=path_to_list.copy(),
            remove_list_item=position_to_delete,
            returns=returns,
            direct_condition=condition,
            **primary_dict,
        )

    def remove_from_set(
        self,
        path_to_set: list,
        items_to_delete: (List[set], set),
        returns: UpdateReturns = UpdateReturns.NONE,
        condition=None,
        **primary_dict,
    ):
        if not isinstance(path_to_set[0], list):
            path_to_set = [path_to_set]
        if not isinstance(items_to_delete, list):
            items_to_delete = [items_to_delete]
        for i, s in enumerate(items_to_delete):
            if not isinstance(s, set):
                items_to_delete[i] = set(s)
        return self.__general_update(
            require_attributes_already_present=True,
            create_item_if_non_existent=False,
            remove_data=path_to_set.copy(),
            remove_set_item=items_to_delete,
            returns=returns,
            direct_condition=condition,
            **primary_dict,
        )

    def delete(self, condition=None, **primary_dict):
        self._primary_key_checker(primary_dict.keys())
        delete_data = {"Key": primary_dict}
        if condition:
            delete_data.update({"ConditionExpression": condition})
        self.__table.delete_item(**delete_data)

    def get_and_delete(self, condition=None, **primary_dict):
        self._primary_key_checker(primary_dict.keys())
        delete_data = {"Key": primary_dict, "ReturnValues": UpdateReturns.ALL_OLD}
        if condition:
            delete_data.update({"ConditionExpression": condition})
        response = self.__table.delete_item(**delete_data)
        return object_with_decimal_to_float(response["Attributes"])

    def scan(self, get_only_primaries: bool = None, attributes_to_get: list = None):
        if attributes_to_get or get_only_primaries:
            if not isinstance(attributes_to_get, list):
                attributes_to_get = []
            expression, name_map = self._create_projection_expression(attributes_to_get)
            response = self.__table.scan(
                ProjectionExpression=expression,
                ExpressionAttributeNames=name_map
            )
        else:
            response = self.__table.scan()
        response["Items"] = [
            object_with_decimal_to_float(item) for item in response["Items"]
        ]
        return response

    def truncate(self):
        with self.__table.batch_writer() as batch:
            for item in self.scan()["Items"]:
                batch.delete_item(Key={key: item[key] for key in self.pk})

    def query(
        self,
        attributes_to_get: list = None,
        max_results: int = None,
        offset_last_key: (str, int, float, dict) = None,
        range_condition: ConditionBase = None,
        index: str = None,
        **query_keys,
    ) -> dict:
        """
        query data based

        Parameters
        ----------
        attributes_to_get: list
            specify the attributes to return (for decreasing transferred data amount)
        max_results: int, optional
            limit the number of items to return
        offset_last_key: str, int, float, dict, optional
            for pagination: if many values provide the last key that shall not be included
        range_condition: ConditionBase, optional
            specify conditions for the range key to match
        index: str, optional
            if query should be executed on index
        query_keys: str
            primary or index keys

        Returns
        -------
        dict
            Count: int, ScannedCount: int, Items: list, (LastEvaluatedKey: (str, int, float))
            items returned, number scanned for operation, actual items, last range key returned (for pagination)

        """
        query_data = dict()
        range_key = None

        if not index:
            query_keys = self._cast_primary_keys(query_keys)
            primary_key = self.pk[0]
            if len(self.pk) > 1:
                range_key = self.pk[1]
        else:
            if offset_last_key is not None and not isinstance(offset_last_key, dict):
                raise TypeError(
                    {
                        "statusCode": 400,
                        "body": "querying on index requires dictionary with last evaluated values",
                        "headers": {"Content-Type": "text/plain"},
                    }
                )
            query_keys = self._cast_index_keys(index, query_keys)
            query_data["IndexName"] = index
            primary_key = self.indexes[index][0]
            if len(self.indexes[index]) > 1:
                range_key = self.indexes[index][1]

        condition_expression_array = [Key(k).eq(v) for k, v in query_keys.items()]
        if range_condition:
            condition_expression_array.append(
                type(range_condition)(Key(range_key), *range_condition._values)
            )

        (
            query_data["KeyConditionExpression"],
            query_data["ExpressionAttributeNames"],
            query_data["ExpressionAttributeValues"],
        ) = _combine_and_conditions(condition_expression_array)

        if attributes_to_get:
            expression, name_map = self._create_projection_expression(
                attributes_to_get, query_data
            )
            query_data["ProjectionExpression"] = expression
            query_data["ExpressionAttributeNames"].update(name_map)
        else:
            query_data["Select"] = SelectReturns.ALL_ATTRIBUTES

        if max_results:
            query_data["Limit"] = max_results
        if offset_last_key:
            if not index:
                start_key = {
                    primary_key: query_keys[primary_key],
                    range_key: offset_last_key,
                }
            else:
                start_key = object_with_float_to_decimal(offset_last_key)
            query_data["ExclusiveStartKey"] = start_key

        response = self.__table.query(**query_data)
        if items := response.get("Items", list()):
            response["Items"] = object_with_decimal_to_float(items)
        if "LastEvaluatedKey" in response:
            response["LastEvaluatedKey"] = object_with_decimal_to_float(
                response["LastEvaluatedKey"]
            )
            if not index:
                response["LastEvaluatedKey"] = response["LastEvaluatedKey"][range_key]
            else:
                response["LastEvaluatedKey"] = response["LastEvaluatedKey"]
        return response

    def __return_dict_of_pk_items_from_multiple_item_response(
        self, object_list: list, convert: bool
    ) -> (dict, list):
        if not convert:
            return object_list
        if len(self.pk) == 1:
            return {item[self.pk[0]]: item for item in object_list}
        return {(item[self.pk[0]], item[self.pk[1]]): item for item in object_list}

    def index_get(
        self,
        index: str,
        return_as_dict_of_primary_keys: bool = False,
        attributes_to_get: list = None,
        **index_keys: dict,
    ):
        """
        get item from index name with index primary

        Parameters
        ----------
        index: str
            the name of the index
        index_keys: dict
            dictionary of the primary_keys
        attributes_to_get: list, optional
            specify certain attributes to get
        return_as_dict_of_primary_keys: bool
            if the response shall be as an array (input=False) or as a dictionary of items
             with primary_values as key (input=True)

        Returns
        -------
        dict
            dynamodb item

        """
        index_keys = self._cast_index_keys(index, index_keys)
        self._index_key_checker(index, index_keys)
        object_list = self.query(
            index=index, attributes_to_get=attributes_to_get, **index_keys
        )["Items"]
        if len(object_list) == 0:
            raise FileNotFoundError
        return self.__return_dict_of_pk_items_from_multiple_item_response(
            object_list, return_as_dict_of_primary_keys
        )

    def batch_get(
        self, primary_keys: Iterable, return_as_dict_of_primary_keys: bool = False
    ) -> dict:
        """
        get all items with given primary keys

        Parameters
        ----------
        primary_keys : Iterable
            primary keys to retrieve items for
        return_as_dict_of_primary_keys: bool
            if the response shall be as an array (input=False) or as a dictionary of items
             with primary_values as key (input=True)

        Returns
        -------
        object with primary_key as key and item as value

        """
        primary_keys = self._cast_primary_keys(primary_keys, batch=True)

        response = _ddb_resource.batch_get_item(
            RequestItems={self.__table_name: {"Keys": primary_keys}}
        )
        object_list = object_with_decimal_to_float(
            response["Responses"][self.__table_name]
        )
        return self.__return_dict_of_pk_items_from_multiple_item_response(
            object_list, return_as_dict_of_primary_keys
        )
