#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2015, Robert Dolega <itiit.robert.dolega@gmail.com>
#
# This ansible module to execute oracle queries


DOCUMENTATION = '''
---
module: oracle
version_added: 0.1
short_description: This ansible module to execute oracle queries.
description:
   - This ansible module to execute oracle queries. The script uses sqlplus.
options: {}
author: Robert Dolega
'''

EXAMPLES = '''
# Execute query
- oracle: oracle_home=/u01/client tnsname=/path/to/tnsnames.ora user=system pass=pass query='select * from dual'
'''

import os


def main():
    module = AnsibleModule(
        argument_spec = dict(
            oracle_home=dict(required=True, default=None),
            tnsname=dict(required=True, default=None),
            user=dict(required=True, default='system'),
            pass=dict(required=True, default='pass'),
            query=dict(required=True, default='select * from dual')
        ),
        supports_check_mode = True
    )
    # TODO almost everything

from ansible.module_utils.basic import *

main()
