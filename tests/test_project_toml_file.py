import unittest
import pathlib as pl


def file_exist():
    path = pl.Path('versions.toml')
    if not path.resolve().is_file():
        raise AssertionError('File does not exist: %s' % str(path))
