# from version_dict import create_dict as c
import json
from unittest.mock import mock_open, patch

import pytest

from version_dict import create_dict

# Mock 3 different files
DEFAULT_MOCK_DATA = "default mock data"
data_dict = {"./x": "{\"key1\": \"value1\"}",
             "./y": "{\"key2\": \"value2\"}",
             "./z": "{\"key2\": \"value3\"}"
             }

data = {'location': {'files': '.'}, 'files': {'x': '>=1'}}

def open_side_effect(name):
    return mock_open(read_data=data_dict.get(name, DEFAULT_MOCK_DATA))()


def test_return_dict():
    assert type(create_dict()) is dict


def test_simple_test(mocker):
    data ['files'] = {'x': '>=1'}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key1': 'value1'}
    assert mock_file.call_count == 1
    mock_file.assert_called_once_with("./x")


def test_skip_first(mocker):
    data ['files'] = {'x': '>=1.3', 'y': '>=1.2'}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key2': 'value2'}
    assert mock_file.call_count == 1
    mock_file.assert_called_once_with("./y")


def test_skip_last(mocker):
    data ['files'] = {'x': '>=1.2', 'y': '>=1.3'}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key1': 'value1'}
    assert mock_file.call_count == 1
    mock_file.assert_called_once_with("./x")


def test_merge_two(mocker):
    data ['files'] = {'x': '>=1', 'y': '>=1'}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key1': 'value1', 'key2': 'value2'}
    assert mock_file.call_count == 2


def test_merge_all(mocker):
    data ['files'] = {'x': '>=1', 'y': '>=1', 'z': '>=1'}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key1': 'value1', 'key2': 'value3'}
    assert mock_file.call_count == 3

testdata = [
    ( {'x': '==1.0.0', 'y': '==1.0.1', 'z': '==1.0.2'}, '1.0.0', {'key1': 'value1'}, 1 ),
    ( {'x': '==1.0.0', 'y': '==1.0.1', 'z': '==1.0.2'}, '1.0.1', {'key2': 'value2'}, 1 ),
    ( {'x': '==1.0.0', 'y': '==1.0.1', 'z': '==1.0.2'}, '1.0.2', {'key2': 'value3'}, 1 ),
    ( {'x': '!=1.0.1', 'y': '>1.0', 'z': '>1.0'}, '1.0.1', {'key2': 'value3'}, 2 )
]

testids = [
    'exactly first',
    'exactly second',
    'exactly third',
    'except first'
]

# @pytest.mark.skip(reason="not ready yet")
@pytest.mark.parametrize('condition, version, result, count', testdata, ids=testids)
def test_various_scenarios(mocker, condition, version, result, count):
    data ['files'] = condition
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict(version)
    assert d == result
    assert mock_file.call_count == count
