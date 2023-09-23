#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pytest
from jsonschema import validate, ValidationError

from pitrix.fixture import db_schema
from pitrix.exceptions import SchemaNotFound
from pitrix.utils.log import logger


class BaseAssert:

    @staticmethod
    def assert_eq(actual_value, expected_value):
        if actual_value == expected_value:
            ...
        else:
            msg = f"eq断言失败，预期结果：{expected_value}，实际结果：{actual_value}"
            logger.error(msg)
            pytest.fail(msg)

    @staticmethod
    def assert_gt(actual_value, expected_value):
        if actual_value > expected_value:
            ...
        else:
            msg = f"gt断言失败，预期结果：{expected_value}，实际结果：{actual_value}"
            logger.error(msg)
            pytest.fail(msg)

    @staticmethod
    def assert_lt(actual_value, expected_value):
        if actual_value < expected_value:
            ...
        else:
            msg = f"lt断言失败，预期结果：{expected_value}，实际结果：{actual_value}"
            logger.error(msg)
            pytest.fail(msg)

    @staticmethod
    def assert_neq(actual_value, expected_value):
        if actual_value != expected_value:
            ...
        else:
            msg = f"neq断言失败，预期结果：{expected_value}，实际结果：{actual_value}"
            logger.error(msg)
            pytest.fail(msg)

    @staticmethod
    def assert_ge(actual_value, expected_value):
        if actual_value >= expected_value:
            ...
        else:
            msg = f"ge断言失败，预期结果：{expected_value}，实际结果：{actual_value}"
            logger.error(msg)
            pytest.fail(msg)

    @staticmethod
    def assert_le(actual_value, expected_value):
        if actual_value <= expected_value:
            ...
        else:
            msg = f"le断言失败，预期结果：{expected_value}，实际结果：{actual_value}"
            logger.error(msg)
            pytest.fail(msg)

    @staticmethod
    def assert_contains(actual_value, expected_value):
        if expected_value in actual_value:
            ...
        else:
            msg = f"contains断言失败，预期结果：{expected_value}，实际结果：{actual_value}"
            logger.error(msg)
            pytest.fail(msg)

    @staticmethod
    def assert_schema(instance, api_name):
        """
        Assert JSON Schema
        :param instance: 请求响应结果
        :param api_name: 存放在schema表中的对应key名
        :return:
        """
        json_schema = db_schema.get(api_name)
        if json_schema is None:
            logger.error('jsonschema未找到！')
            raise SchemaNotFound(api_name)
        try:
            validate(instance, schema=json_schema)
        except ValidationError as msg:
            logger.error(msg)
            raise AssertionError


case = BaseAssert()
