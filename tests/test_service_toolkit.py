from aegisrover.service.admin_tools import request_id
from aegisrover.service.toolkit import canonical_query


def test_request_id_ignores_json_field_order():
    body = {'mission': 'm1', 'params': {'speed': 2, 'heading': 90}, 'priority': 1}
    reordered = {'priority': 1, 'params': {'heading': 90, 'speed': 2}, 'mission': 'm1'}

    assert request_id('POST', '/missions', body) == request_id('POST', '/missions', reordered)


def test_request_id_changes_with_request_content():
    assert request_id('POST', '/missions', {'a': 1}) != request_id('POST', '/missions', {'a': 2})
    assert request_id('POST', '/missions', {'a': 1}) != request_id('GET', '/missions', {'a': 1})


def test_canonical_query_ignores_parameter_order():
    assert canonical_query({'b': 2, 'a': 1}) == canonical_query({'a': 1, 'b': 2})
    assert canonical_query({'b': 2, 'a': 1}) == 'a=1&b=2'


def test_canonical_query_encodes_values():
    assert canonical_query({'name': 'a b', 'x': '1/2'}) == 'name=a+b&x=1%2F2'
