#!/usr/bin/env python3

import os
import sys
import pprint
from urllib.request import Request, urlopen


def main(license_name):
    license_url_tpl = 'https://github.com/myles/licenses/raw/master/{}.txt'

    shortcuts = {
        'bsd': 'bsd-3-clause-clear',
        'cc0': 'cc0-1.0',
        'gpl': 'gpl-3.0'
    }

    if shortcuts.get(license_name):
        license_name = shortcuts.get(license_name)

    req = Request(license_url_tpl.format(license_name))
    res = urlopen(req)

    print(res.read().decode('UTF-8'))


if __name__ == '__main__':
    main(sys.argv[1])
