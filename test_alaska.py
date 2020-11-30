# -*- coding: utf-8 -*-

import pytest
import requests
import urlparse


def test_create_polar_bear(foptions, endpoint='/bear'):
    bear = foptions['default_bear']
    url = urlparse.urljoin(foptions['url'], endpoint)
    r = requests.post(url=url, json=bear)
    assert r.status_code == 200
    assert int(r.text) >= 1