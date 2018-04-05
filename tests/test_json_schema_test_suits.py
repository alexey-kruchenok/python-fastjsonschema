from __future__ import with_statement
from __future__ import absolute_import
import json
from pathlib import Path

import pytest

from fastjsonschema import CodeGenerator, JsonSchemaException, compile


def pytest_generate_tests(metafunc):
    suite_dir = u'JSON-Schema-Test-Suite/tests/draft4'
    ignored_suite_files = [
        u'definitions.json',
        u'dependencies.json',
        u'ecmascript-regex.json',
        u'ref.json',
        u'refRemote.json',
        u'uniqueItems.json',
    ]

    suite_dir_path = Path(suite_dir).resolve()
    test_file_paths = sorted(set(suite_dir_path.glob(u"**/*.json")))

    param_values = []
    param_ids = []

    for test_file_path in test_file_paths:
        with test_file_path.open() as test_file:
            test_cases = json.load(test_file)
            for test_case in test_cases:
                for test_data in test_case[u'tests']:
                    param_values.append(pytest.param(
                        test_case[u'schema'],
                        test_data[u'data'],
                        test_data[u'valid'],
                        marks=pytest.mark.xfail if test_file_path.name in ignored_suite_files else pytest.mark.none,
                    ))
                    param_ids.append(u'{} / {} / {}'.format(
                        test_file_path.name,
                        test_case[u'description'],
                        test_data[u'description'],
                    ))

    metafunc.parametrize([u'schema', u'data', u'is_valid'], param_values, ids=param_ids)


def test(schema, data, is_valid):
    # For debug purposes. When test fails, it will print stdout.
    print CodeGenerator(schema).func_code

    validate = compile(schema)
    try:
        result = validate(data)
        print u'Validate result:', result
    except JsonSchemaException:
        if is_valid:
            raise
    else:
        if not is_valid:
            pytest.fail(u'Test should not pass')
