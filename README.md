# version-dict

This module creates a version dependent dictionary following [pep508](https://www.python.org/dev/peps/pep-0508/) syntax.

The configuration file `versions.toml` contains a file location and a list of files containing dictionary items which will be merged in chronological order according to their target version, also specified in the same file.
