#!/usr/bin/env python3
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    print(os.getenv('SMARTCAST_VERSION'))


if __name__ == '__main__':
    main()
