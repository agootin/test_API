import pytest
import requests
from src.baseclasses.response import Response
from src.schemas.user import User
from tests.configuration import API_URL_AUTH
from tests.configuration import TIMEOUT


def test_get_user_with_token(generate_auth_token):
    """
    Получение информации о владельце переданного x-token
    """
    url = f'{API_URL_AUTH}/me'
    headers = {'x-token': generate_auth_token}
    response = Response(requests.get(url, headers=headers, timeout=TIMEOUT))
    response.assert_status_code(200)


@pytest.mark.parametrize('x_token', ['', 'xxx'])
def test_get_user_with_invalid_token(x_token):
    url = f'{API_URL_AUTH}/me'
    headers = {'x-token': x_token}
    response = Response(requests.get(url, headers=headers, timeout=TIMEOUT))
    response.assert_status_code(403)
