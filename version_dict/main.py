import json
import os

import toml
from packaging import specifiers, version

FILE_NAME = 'versions.toml'


def create_dict(current_version='') -> dict:
    if current_version == '':
        current_version = version.Version(os.getenv('FOR_VERSION'))
    configuration = toml.load(FILE_NAME)
    # files location
    location = configuration['location']['files']
    # sorted file names
    vers_dict = {}
    for file_name, target_version in configuration['files'].items():
        target_version = configuration['files'][file_name]
        if specifiers.SpecifierSet(target_version).contains(current_version):
            with open(f'{location}/{file_name}') as json_file:
                dict_to_add = json.load(json_file)
            vers_dict = {**vers_dict, **dict_to_add}
    return vers_dict
