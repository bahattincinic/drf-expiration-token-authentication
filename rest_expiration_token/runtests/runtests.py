#!/usr/bin/env python
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'rest_expiration_token.runtests.settings'

import django
from django.conf import settings
from django.test.utils import get_runner


def main():
    try:
        django.setup()
    except AttributeError:
        pass
    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    module_name = 'rest_expiration_token.tests'
    if django.VERSION[0] == 1 and django.VERSION[1] < 6:
        module_name = 'rest_expiration_token'

    failures = test_runner.run_tests([module_name])
    sys.exit(failures)


if __name__ == '__main__':
    main()
