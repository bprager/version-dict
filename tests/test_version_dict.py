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
  d = create_dict()
  assert d == {'key': 'value'}

def test_files_sorted(mocker):
  data={'location': {'files': '.'}, 'files': {'x': '>=1'}}
  mocker.patch('toml.load', return_value=data)
  data='{"key02": "value02",  "key01": "value01"}'
  mocker.patch('builtins.open', mocker.mock_open(read_data=data))
  d = create_dict()
  assert d == {'key01': 'value01', 'key02': 'value02'}
