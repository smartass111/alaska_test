# -*- coding: utf-8 -*-

import pytest
import requests
import urlparse


def test_negative_add_bear_without_age(foptions, endpoint='/bear'):
    bear = foptions['default_bear'].copy()
    bear.pop('bear_age', None)
    url = urlparse.urljoin(foptions['url'], endpoint)
    r = requests.post(url=url, json=bear)
    assert r.status_code == 200
    assert r.text == "Error. Pls fill all parameters"


def test_negative_add_bear_invalid_json(foptions, endpoint='/bear'):
    bear_str = '{"bear_type": '
    url = urlparse.urljoin(foptions['url'], endpoint)
    r = requests.post(url=url, data=bear_str)
    assert r.status_code == 200
    #assert r.text == "Error"