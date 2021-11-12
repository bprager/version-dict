# from version_dict import create_dict as c
from version_dict import create_dict

def test_create_dict():
    assert type(create_dict()) is dict
