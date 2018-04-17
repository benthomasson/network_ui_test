#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    coverage_report [options] <server>

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
import os
import requests
import subprocess
import json

logger = logging.getLogger('coverage_report')

TESTS_API = '/network_ui_test/tests'


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = docopt(__doc__, args)
    if parsed_args['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    elif parsed_args['--verbose']:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    server = parsed_args['<server>']
    tests = requests.get(server + TESTS_API, verify=False).json()

    tests_with_coveage = []

    load_data = None

    for test in tests['tests']:
        if test['name'] == 'Load':
            response = requests.get(server + test['coverage'], verify=False)
            if response.ok:
                load_data = json.loads(response.text)

    for test in tests['tests']:
        response = requests.get(server + test['coverage'], verify=False)
        if response.ok:
            if not os.path.exists(test['name']):
                os.mkdir(test['name'])
            with open(test['name'] + "/coverage.json", 'w') as file:
                test_data = json.loads(response.text)
                for f in test_data.keys():
                    for i in load_data[f]['b']:
                        if i not in test_data[f]['b']:
                            test_data[f]['b'][i] = load_data[f]['b'][i]
                            test_data[f]['branchMap'][i] = load_data[f]['branchMap'][i]
                    for i in load_data[f]['f']:
                        if i not in test_data[f]['f']:
                            test_data[f]['f'][i] = load_data[f]['f'][i]
                            test_data[f]['fnMap'][i] = load_data[f]['fnMap'][i]
                    for i in load_data[f]['s']:
                        if i not in test_data[f]['s']:
                            test_data[f]['s'][i] = load_data[f]['s'][i]
                            test_data[f]['statementMap'][i] = load_data[f]['statementMap'][i]
                file.write(json.dumps(test_data, sort_keys=True, indent=4))
                tests_with_coveage.append(test)

    for test in tests_with_coveage:
        subprocess.Popen('istanbul report html', shell=True, cwd=test['name']).wait()
    subprocess.Popen('istanbul report html', shell=True).wait()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
