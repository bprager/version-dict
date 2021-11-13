import os
import toml
from pep508_parser import parser
from packaging import version

FILE_NAME = 'versions.toml'

def create_dict() -> dict:
  vers_dict = {}
  current_version = os.getenv('FOR_VERSION')
  dict_files=toml.load(FILE_NAME)['files']
  for file_name, target_version in dict_files.items():
    if fit(current_version=current_version, target_version=target_version):
      pass
  return vers_dict

def fit(current_version: str, target_version: str) -> bool:
  required = parser.parse(f'version{target_version}')[2]
  return compare(current_version, required)

def compare(current_version: str, required: list) -> bool:
  c = version.parse(current_version) # current version
  for comparator, target in required:
    t = version.parse(target) # target version
    if comparator == '~=':    # compatible release clause
      # as of PEP440 is eqivalent with '>= V.N, == V.*'
      if (c < t): return False
      next
    elif comparator == '==':  # version matching clause
      if (c != t): return False
      next
    elif comparator == '!=':  # version exlusion clause
      if (c == t): return False
      next
    elif comparator == '<=':  # inclusive ordered less than clause
      if (c > t): return False
      next
    elif comparator == '>=':  # inclusive ordered greater than clause
      if (c < t): return False
      next
    elif comparator == '<':   # exclusive ordered less than clause
      if (c >= t): return False
      next
    elif comparator == '>':   # exlusive ordered greater than clause
      if (c <= t): return False
      next
    elif comparator == '===': # arbitrary equality clause
      if (current_version != target): return False
      next
    else:
      raise ValueError(f'Unknown comparision operator: {comparator}!')
  return True
