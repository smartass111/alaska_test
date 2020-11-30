# -*- coding: utf-8 -*-

import pytest
import requests
import urlparse
import json
import random


def helper_get_ids(foptions, endpoint='/bear'):
    url = urlparse.urljoin(foptions['url'], endpoint)
    r = requests.get(url=url)
    bears = json.loads(r.text)
    return [bear['bear_id'] for bear in bears]


@pytest.mark.parametrize('execution_number', range(3))
def test_create_bear(execution_number, foptions, endpoint='/bear'):
    bear = foptions['default_bear']
    url = urlparse.urljoin(foptions['url'], endpoint)
    r = requests.post(url=url, json=bear)
    assert r.status_code == 200
    assert int(r.text) >= 1


@pytest.mark.dependency(depends=['test_create_bear'])
def test_delete_bear(foptions, endpoint='/bear/'):
    bear_id = random.choice(helper_get_ids(foptions))
    url = urlparse.urljoin(foptions['url'], endpoint)
    url = urlparse.urljoin(url, str(bear_id))
    r = requests.delete(url)
    assert r.status_code == 200
    assert r.text == 'OK'


@pytest.mark.dependency(depends=['test_create_bear'])
def test_update_bear(foptions, endpoint='/bear/'):
    bear_id = random.choice(helper_get_ids(foptions))
    url = urlparse.urljoin(foptions['url'], endpoint)
    url = urlparse.urljoin(url, str(bear_id))
    bear = foptions['default_bear']
    bear['bear_age'] = 13
    r = requests.put(url, json=bear)
    assert r.status_code == 200
    assert r.text == 'OK'


@pytest.mark.dependency(depends=['test_update_bear', 'test_delete_bear'])
def test_delete_all_bears(foptions, endpoint='/bear'):
    url = urlparse.urljoin(foptions['url'], endpoint)
    r = requests.delete(url)
    assert r.status_code == 200
    assert r.text == 'OK'


@pytest.mark.dependency(depends=['test_delete_all_bears'])
def test_check_bear_list_empty(foptions, endpoint='/bear'):
    url = urlparse.urljoin(foptions['url'], endpoint)
    r = requests.get(url)
    assert r.status_code == 200
    assert r.text == '[]'
