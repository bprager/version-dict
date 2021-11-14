import unittest
import pathlib as pl
import toml

FILE_NAME = 'versions.toml'

def test_file_exist():
    path = pl.Path(FILE_NAME)
    if not path.resolve().is_file():
        raise AssertionError('File does not exist: %s' % str(path))

def test_contains_location():
    dict_files = toml.load(FILE_NAME)
    assert 'location' in dict_files
    assert dict_files['location']

def test_contains_files():
    dict_files = toml.load(FILE_NAME)
    assert 'files' in dict_files
    assert dict_files['files']
