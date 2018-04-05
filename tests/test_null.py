
from __future__ import absolute_import
import pytest

from fastjsonschema import JsonSchemaException


exc = JsonSchemaException(u'data must be null')
@pytest.mark.parametrize(u'value, expected', [
    (0, exc),
    (None, None),
    (True, exc),
    (u'abc', exc),
    ([], exc),
    ({}, exc),
])
def test_null(asserter, value, expected):
    asserter({u'type': u'null'}, value, expected)
