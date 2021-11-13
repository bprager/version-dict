import os
from unittest import mock


def test_check_standard_version():
    assert os.getenv('FOR_VERSION') == '1.2.3'


def test_check_custom_version():
    with mock.patch.dict(os.environ, {'FOR_VERSION': '3.4.5'}):
        assert os.getenv('FOR_VERSION') == '3.4.5'
