
from __future__ import absolute_import
import pytest

from fastjsonschema import JsonSchemaException


@pytest.fixture(params=[u'number', u'integer'])
def number_type(request):
    return request.param


exc = JsonSchemaException(u'data must be {number_type}')
@pytest.mark.parametrize(u'value, expected', [
    (-5, -5),
    (0, 0),
    (5, 5),
    (None, exc),
    (True, exc),
    (u'abc', exc),
    ([], exc),
    ({}, exc),
])
def test_number(asserter, number_type, value, expected):
    if isinstance(expected, JsonSchemaException):
        expected = JsonSchemaException(expected.message.format(number_type=number_type))
    asserter({u'type': number_type}, value, expected)


exc = JsonSchemaException(u'data must be smaller than or equal to 10')
@pytest.mark.parametrize(u'value, expected', [
    (-5, -5),
    (5, 5),
    (9, 9),
    (10, 10),
    (11, exc),
    (20, exc),
])
def test_maximum(asserter, number_type, value, expected):
    asserter({
        u'type': number_type,
        u'maximum': 10,
    }, value, expected)


exc = JsonSchemaException(u'data must be smaller than 10')
@pytest.mark.parametrize(u'value, expected', [
    (-5, -5),
    (5, 5),
    (9, 9),
    (10, exc),
    (11, exc),
    (20, exc),
])
def test_exclusive_maximum(asserter, number_type, value, expected):
    asserter({
        u'type': number_type,
        u'maximum': 10,
        u'exclusiveMaximum': True,
    }, value, expected)


exc = JsonSchemaException(u'data must be bigger than or equal to 10')
@pytest.mark.parametrize(u'value, expected', [
    (-5, exc),
    (9, exc),
    (10, 10),
    (11, 11),
    (20, 20),
])
def test_minimum(asserter, number_type, value, expected):
    asserter({
        u'type': number_type,
        u'minimum': 10,
    }, value, expected)


exc = JsonSchemaException(u'data must be bigger than 10')
@pytest.mark.parametrize(u'value, expected', [
    (-5, exc),
    (9, exc),
    (10, exc),
    (11, 11),
    (20, 20),
])
def test_exclusive_minimum(asserter, number_type, value, expected):
    asserter({
        u'type': number_type,
        u'minimum': 10,
        u'exclusiveMinimum': True,
    }, value, expected)


exc = JsonSchemaException(u'data must be multiple of 3')
@pytest.mark.parametrize(u'value, expected', [
    (-4, exc),
    (-3, -3),
    (-2, exc),
    (-1, exc),
    (0, 0),
    (1, exc),
    (2, exc),
    (3, 3),
    (4, exc),
    (5, exc),
    (6, 6),
    (7, exc),
])
def test_multiple_of(asserter, number_type, value, expected):
    asserter({
        u'type': number_type,
        u'multipleOf': 3,
    }, value, expected)


@pytest.mark.parametrize(u'value', (
    1.0,
    0.1,
    0.01,
    0.001,
))
def test_integer_is_not_number(asserter, value):
    asserter({
        u'type': u'integer',
    }, value, JsonSchemaException(u'data must be integer'))


@pytest.mark.parametrize(u'value', (
    1.0,
    0.1,
    0.01,
    0.001,
))
def test_number_allows_float(asserter, value):
    asserter({
        u'type': u'number',
    }, value, value)
