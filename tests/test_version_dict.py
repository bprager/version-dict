# from version_dict import create_dict as c
from version_dict import create_dict
import pytest
import json
from unittest.mock import patch, mock_open

def test_return_dict():
    assert type(create_dict()) is dict

def test_simple_test(mocker):
  data={'location': {'files': '.'}, 'files': {'x': '>=1'}}
  mocker.patch('toml.load', return_value=data)
  data='{"key": "value"}'
  mocker.patch('builtins.open', mocker.mock_open(read_data=data))
  d = create_dict('1.2.3')
  assert d == {'key': 'value'}

def test_skip_first(mocker):
  data={'location': {'files': '.'}, 'files': {'x': '>=1.3', 'y': '>=1.2'}}
  mocker.patch('toml.load', return_value=data)
  data='{"key": "value"}'
  with patch("builtins.open", mock_open(read_data=data)) as mock_file:
    d = create_dict('1.2.3')
  assert d == {'key': 'value'}
  mock_file.assert_called_once_with("./y")
  assert mock_file.call_count == 1

def test_skip_last(mocker):
  data={'location': {'files': '.'}, 'files': {'x': '>=1.2', 'y': '>=1.3'}}
  mocker.patch('toml.load', return_value=data)
  data='{"key": "value"}'
  with patch("builtins.open", mock_open(read_data=data)) as mock_file:
    d = create_dict('1.2.3')
  assert d == {'key': 'value'}
  mock_file.assert_called_once_with("./x")
  assert mock_file.call_count == 1
