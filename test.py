#!/usr/bin/env python3
import os
from datetime import datetime

from appium.webdriver.common.mobileby import MobileBy
from dotenv import load_dotenv

import version_dict


def main():
    load_dotenv()
    version=(os.getenv('FOR_VERSION'))
    dict = version_dict.create_dict(version)

    if (version != '42'):
      print('vizio_sign_in: ' + ' '.join(str(e) for e in dict['vizio_sign_in']))
    else:
      print(dict['current_date'] % datetime.now())
      print('vizio_sign_in: ' + ' '.join(str(e) for e in dict['vizio_sign_in']) % { 'MobileBy.ID': MobileBy.ID })


if __name__ == '__main__':
    main()
