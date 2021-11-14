#!/usr/bin/env python3
import os

from dotenv import load_dotenv

import version_dict


def main():
    load_dotenv()
    version=(os.getenv('FOR_VERSION'))
    print(version_dict.create_dict(version))


if __name__ == '__main__':
    main()
