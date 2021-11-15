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


def open_side_effect(name):
    return mock_open(read_data=data_dict.get(name, DEFAULT_MOCK_DATA))()


def test_return_dict():
    assert type(create_dict()) is dict


def test_simple_test(mocker):
    data = {'location': {'files': '.'}, 'files': {'x': '>=1'}}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key1': 'value1'}
    assert mock_file.call_count == 1
    mock_file.assert_called_once_with("./x")


def test_skip_first(mocker):
    data = {'location': {'files': '.'}, 'files': {'x': '>=1.3', 'y': '>=1.2'}}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key2': 'value2'}
    assert mock_file.call_count == 1
    mock_file.assert_called_once_with("./y")


def test_skip_last(mocker):
    data = {'location': {'files': '.'}, 'files': {'x': '>=1.2', 'y': '>=1.3'}}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key1': 'value1'}
    assert mock_file.call_count == 1
    mock_file.assert_called_once_with("./x")


def test_merge_two(mocker):
    data = {'location': {'files': '.'}, 'files': {'x': '>=1', 'y': '>=1'}}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key1': 'value1', 'key2': 'value2'}
    assert mock_file.call_count == 2


def test_merge_all(mocker):
    data = {'location': {'files': '.'}, 'files': {
        'x': '>=1', 'y': '>=1', 'z': '>=1'}}
    mocker.patch('toml.load', return_value=data)
    with patch("builtins.open", side_effect=open_side_effect) as mock_file:
        d = create_dict('1.2.3')
    assert d == {'key1': 'value1', 'key2': 'value3'}
    assert mock_file.call_count == 3
