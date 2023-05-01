import pytest
import requests
from src.baseclasses.response import Response
from src.schemas.user import User
from tests.configuration import API_URL_USERS
from tests.configuration import TIMEOUT


def test_users_limit():
    url = API_URL_USERS
    params = {"limit": 1}
    response = Response(requests.get(url, params=params, timeout=TIMEOUT))
    response.response_json = response.response_json.get('data')
    response.assert_status_code(200)
    assert len(response.response_json) <= 1, "параметр 'limit' неправильно ограничивает выдачу"


def test_user_create(create_user):
    response = Response(create_user)
    response.assert_status_code(201).validate_by_schema(User)
    print(response.response_json)


def test_user_create_inactive_company_id():
    """
    Создание пользователя с привязкой к неактивной компании
    """
    url = API_URL_USERS
    payload = {
        'last_name': "string",
        "company_id": 6
    }
    response = Response(requests.post(url, json=payload, timeout=TIMEOUT))
    response.assert_status_code(400)


def test_user_create_only_mandatory_fields():
    """
    Создание пользователя с указанием только обязательных полей
    """
    url = API_URL_USERS
    payload = {
        'last_name': "string",
    }
    response = Response(requests.post(url, json=payload, timeout=TIMEOUT))
    response.assert_status_code(201).validate_by_schema(User)


def test_get_user_by_id(create_user, delete_user):
    user_id = create_user.json()['user_id']
    url = f'{API_URL_USERS}/{user_id}'
    response = Response(requests.get(url, timeout=TIMEOUT))
    response.assert_status_code(200).validate_by_schema(User)
    delete_user(user_id)


def test_update_user_by_id(create_user, delete_user):
    user_id = create_user.json()['user_id']
    url = f'{API_URL_USERS}/{user_id}'
    updated_last_name = 'string1'
    payload = {
        'last_name': updated_last_name,
    }
    response = Response(requests.put(url, json=payload, timeout=TIMEOUT))
    response.assert_status_code(200).validate_by_schema(User).validate_field("last_name", updated_last_name)
    delete_user(user_id)


def test_delete_user_by_id(create_user, delete_user):
    user_id = create_user.json()['user_id']
    response = Response(delete_user(user_id))
    response.assert_status_code(202)


def test_delete_absent_user_by_id(delete_user):
    user_id = 0
    response = Response(delete_user(user_id))
    response.assert_status_code(404)

