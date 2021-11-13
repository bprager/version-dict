import unittest
import pathlib as pl

FILE_NAME = 'versions.toml'

def file_exist():
    path = pl.Path(FILE_NAME)
    if not path.resolve().is_file():
        raise AssertionError('File does not exist: %s' % str(path))
