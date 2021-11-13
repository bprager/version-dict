#!/usr/bin/env python3
import os

from dotenv import load_dotenv

import version_dict


def main():
    load_dotenv()
    print(os.getenv('FOR_VERSION'))


if __name__ == '__main__':
    main()
