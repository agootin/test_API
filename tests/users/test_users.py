from src.basaclasses.response import Response
from src.schemas.user import User

# def test_2():
#     resp = requests.get(SERVICE_URL)
#     print(resp.json())


def test_getting_users_list(get_users):
    Response(get_users).assert_status_code(200).validate(User)
