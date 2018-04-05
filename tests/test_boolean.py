
from __future__ import absolute_import
import pytest

from fastjsonschema import JsonSchemaException


exc = JsonSchemaException(u'data must be boolean')
@pytest.mark.parametrize(u'value, expected', [
    (0, exc),
    (None, exc),
    (True, True),
    (False, False),
    (u'abc', exc),
    ([], exc),
    ({}, exc),
])
def test_boolean(asserter, value, expected):
    asserter({u'type': u'boolean'}, value, expected)
