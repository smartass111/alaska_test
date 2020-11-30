# -*- coding: utf-8 -*-

import pytest
import urlparse


def pytest_addoption(parser):
    parser.addoption('--target-port', metavar='target_port', default='8091', type=str, help='endpoint port')
    parser.addoption('--target-host', metavar='target_host', default='127.0.0.1', type=str, help='endpoint web address')


@pytest.fixture(autouse=True, scope='session')
def foptions(request):
    test_args={}
    test_args['target_host'] = request.config.getoption('--target-host')
    test_args['target_port'] = request.config.getoption('--target-port')
    host = "http://" + test_args['target_host'] if not test_args['target_host'].startswith("http://") else test_args['target_host']
    test_args['url'] = host + ":" + test_args['target_port']
    test_args['allowed_bear_types'] = ("POLAR", "BROWN", "BLACK", "GUMMY")
    test_args['default_bear'] = {"bear_type": "BLACK", "bear_name": "mikhail", "bear_age": 17.5}
    yield test_args