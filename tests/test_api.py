import pytest
from unittest.mock import Mock
import client.logic

TODOS_MAX = 200


@pytest.fixture
def response_mock():
    return Mock()


def test_success(response_mock):
    response_mock.status_code = 200
    client.logic.check_response(response_mock)


@pytest.mark.parametrize('todos_id', [1, TODOS_MAX])
def test_getting_a_resource_positive(todos_id):
    assert client.logic.getting_a_resource_positive().json().get('status_code') == 200
    if todos_id == 1:
        assert client.logic.getting_a_resource_positive().json()['id'][0] == todos_id
    if todos_id == TODOS_MAX:
        assert client.logic.getting_a_resource_positive().json()['id'][1] == TODOS_MAX


@pytest.mark.parametrize('todos_id', [-1, 0, TODOS_MAX + 1])
def test_getting_a_resource_negative(todos_id):
    assert client.logic.getting_a_resource_negative().json().get('status_code') == 404


def test_creating_a_resource():
    title = 'theme'
    completed = 'true'

    assert client.logic.creating_a_resource().json().get('status_code') == 201
    assert client.logic.creating_a_resource().json().get('id') == TODOS_MAX + 1
    assert client.logic.creating_a_resource().json().get('userId') == 1
    assert client.logic.creating_a_resource().json().get('title') == title
    assert client.logic.creating_a_resource().json().get('completed') == completed


def test_updating_a_resource_with_put_positive():
    title = 'foo'
    completed = 'true'

    assert client.logic.updating_a_resource_with_put_positive().json().get('status_code') == 200
    assert client.logic.updating_a_resource_with_put_positive().json().get('title') == title
    assert client.logic.updating_a_resource_with_put_positive().json().get('completed') == completed


def test_updating_a_resource_with_put_negative():
    assert client.logic.updating_a_resource_with_put_negative().json().get('status_code') == 500


def test_updating_a_resource_with_patch_positive():
    completed = 'true'

    assert client.logic.updating_a_resource_with_patch_positive().json().get('status_code') == 200
    assert client.logic.updating_a_resource_with_patch_positive().json().get('completed') == completed
