from requests import Response
from unittest.mock import Mock

from client.exceptions import RequestRateException, NotFoundException


def check_response(response: Response):
    if response.status_code == 429:
        raise RequestRateException()
    elif response.status_code == 404:
        raise NotFoundException()


def getting_a_resource_positive():
    resource = {'status_code': 200, 'id': [1, 200]}
    response = Mock(**{'json.return_value': resource})
    return response


def getting_a_resource_negative():
    resource = {'status_code': 404}
    response = Mock(**{'json.return_value': resource})
    return response


def creating_a_resource():
    resource = {'status_code': 201,
                'id': 201,
                'title': 'theme',
                'completed': 'true',
                'userId': 1
                }

    response = Mock(**{'json.return_value': resource})
    return response


def updating_a_resource_with_put_positive():
    resource = {'status_code': 200,
                'title': 'foo',
                'completed': 'true',
                }

    response = Mock(**{'json.return_value': resource})
    return response


def updating_a_resource_with_put_negative():
    resource = {'status_code': 500}

    response = Mock(**{'json.return_value': resource})
    return response


def updating_a_resource_with_patch_positive():
    resource = {'status_code': 200,
                'completed': 'true'}

    response = Mock(**{'json.return_value': resource})
    return response
