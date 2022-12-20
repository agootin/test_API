import requests
from .configuration import SERVICE_URL
from src.basaclasses.response import Response
from src.schemas.user import User

# def test_2():
#     resp = requests.get(SERVICE_URL)
#     print(resp.json())


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response=response)
    test_object.assert_status_code(200).validate(User)
