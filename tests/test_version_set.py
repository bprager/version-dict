import os
from unittest import mock


def test_check_standard_version():
    assert os.getenv('SMARTCAST_VERSION') == '3.1.2'


def test_check_custom_version():
    with mock.patch.dict(os.environ, {'SMARTCAST_VERSION': 'x.x.x'}):
        assert os.getenv('SMARTCAST_VERSION') == 'x.x.x'
