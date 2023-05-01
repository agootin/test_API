import pytest
import requests

from tests.configuration import API_URL_AUTH, API_URL_USERS, TIMEOUT


@pytest.fixture()
def generate_auth_token():
    url = f'{API_URL_AUTH}/authorize'
    payload = {
        "login": "string1",
        "password": "qwerty12345",
        "timeout": 360
    }
    response = requests.post(url, json=payload)
    return response.json()['token']


@pytest.fixture()
def create_user():
    url = API_URL_USERS
    payload = {
        "first_name": "testing",
        'last_name': "testing",
        "company_id": 1
    }
    response = requests.post(url, json=payload, timeout=TIMEOUT)
    return response


def delete_user_method(user_id):
    url = f'{API_URL_USERS}/{user_id}'
    response = requests.delete(url, timeout=TIMEOUT)
    return response


@pytest.fixture()
def delete_user():
    return delete_user_method


