#!/usr/bin/env python3

"""
Converts the license template files to the actual LICENSE files.

Requirments:
- Jinja2
"""

from os import chdir
from glob import iglob
from datetime import datetime
from os.path import dirname, realpath, join, basename

import frontmatter
from jinja2 import Template

FULL_NAME = 'Myles Braithwaite'
EMAIL = 'me@mylesbraithwatie.com'
COMPANY_NAME = 'Myles Braithwaite Ltd.'


def main():
    root_dir = join(dirname(realpath(__file__)), '../')

    chdir(root_dir)
    tpl_files = iglob('_licenses/*.txt')

    for tpl_file in tpl_files:
        context = {
            'full_name': FULL_NAME,
            'company_name': COMPANY_NAME,
            'email': EMAIL,
            'now': datetime.now()
        }

        with open(tpl_file, 'r') as fobj:
            license = frontmatter.loads(fobj.read())

        tpl = Template(license.content)

        with open(join(root_dir, basename(tpl_file)), 'w') as fobj:
            fobj.write(tpl.render(**context))


if __name__ == '__main__':
    main()
