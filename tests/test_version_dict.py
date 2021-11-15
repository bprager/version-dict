# from version_dict import create_dict as c
from version_dict import create_dict
import pytest
import json
from unittest.mock import patch, mock_open

DEFAULT_MOCK_DATA = "default mock data"
data_dict = {'x': '"{\"key1\": \"value1\"}"',
             'y': '"{\"key2\": \"value2\"}"',
             'z': '"{\"key2\": \"another_value2\"}"'}

def open_side_effect(name):
    return mock_open(read_data=data_dict.get(name, DEFAULT_MOCK_DATA))()

def test_return_dict():
    assert type(create_dict()) is dict

def test_simple_test(mocker):
  data={'location': {'files': '.'}, 'files': {'x': '>=1'}}
  mocker.patch('toml.load', return_value=data)
  data='{"key": "value"}'
  mocker.patch('builtins.open', mocker.mock_open(read_data=data))
  d = create_dict('1.0')
  assert d == {'key': 'value'}

@pytest.mark.skip(reason="not ready yet")
def test_skip_last_version(mocker):
  data={'location': {'files': '.'}, 'files': {'x': '>=1.0', 'y': '>=2.0'}}
  mocker.patch('toml.load', return_value=data)
  data='{"key": "value"}'
  mocker.patch('builtins.open', side_effect=open_side_effect)
  d = create_dict()
  assert d == {'key': 'value'}
