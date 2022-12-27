import pytest
import requests
from tests.configuration import SERVICE_URL


@pytest.fixture()
def get_users():
    response = requests.get(SERVICE_URL)
    return response
