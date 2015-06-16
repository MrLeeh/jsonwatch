"""
    Copyright © 2015 by Stefan Lehmann

"""

import pytest
from jsonwatch.jsonvalue import JsonValue
from jsonwatch.jsonobject import JsonObject


nested_json_string = ('\n'
                      '    {\n'
                      '        "item1": 1,\n'
                      '        "item2": 2,\n'
                      '        "item3": {\n'
                      '            "item1": 1,\n'
                      '            "item2": 2\n'
                      '        }\n'
                      '    }')


@pytest.fixture
def nested_json():
    from jsonwatch.jsonobject import JsonObject
    node = JsonObject('root')
    node.from_json(nested_json_string)
    return node

def test_item_eq(nested_json):
    node = nested_json

    # same object
    item1 = node['item1']
    assert item1 == node['item1']

    # same key, no parent
    item1 = JsonValue('item1', 1)
    assert not item1 == node['item1']

    # same key, different parent
    item1 = node['item3']['item1']
    assert not item1 == node['item1']

