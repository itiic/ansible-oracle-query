#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2015, Robert Dolega
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
import json
from subprocess import Popen, PIPE


def runSqlQuery(sqlCommand, connectString, oracleHome):
   session = Popen(oracleHome + '/bin/sqlplus', '-S', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
   session.stdin.write(sqlCommand)
   return session.communicate()


def main():
    global module
    module = AnsibleModule(
        argument_spec = dict(
            oracleHome=dict(required=True, default=None, type='str'),
            connectString=dict(required=True, default=None, type='str'),
            scriptPath=dict(required=True, default=None, type='str')
        ),
        supports_check_mode = True
    )

    # global vars
    oracleHome = module.params['oracleHome']

    # user/pass@SID
    connectString = module.params['connectString']

    # path to script
    scriptPath = module.params['scriptPath']

    # set ORACLE_HOME environment variable
    os.environ['ORACLE_HOME'] = oracleHome
    # = @ +  path
    sqlCommand = '@'+scriptPath

    # execution
    queryResult, errorMessage = runSqlQuery(sqlCommand, connectString, oracleHome)

    # TODO 1. Output to json
    # TODO 2. Error handler
    # TODO 3. Test it :)

    module.exit_json(
        changed=changed,
        key=key,
        type=argument_type,
        value=value,
        old_value=old_value
    )

from ansible.module_utils.basic import *

main()
