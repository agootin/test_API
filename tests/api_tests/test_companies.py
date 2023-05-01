import pytest
import requests
from src.baseclasses.response import Response
from src.enums.global_enums import Statuses
from src.schemas.company import Company
from tests.configuration import API_URL_COMPANIES
from tests.configuration import TIMEOUT


def test_get_companies_list():
    url = API_URL_COMPANIES
    response = Response(requests.get(url, timeout=TIMEOUT))
    response.response_json = response.response_json.get('data')
    response.assert_status_code(200).validate_by_schema(Company)


@pytest.mark.parametrize("status", [status for status in Statuses])
def test_companies_filtering_by_status(status):
    """
    Проверка фильтрации по параметру status
    """
    url = API_URL_COMPANIES
    params = {"status": status.value}
    response = Response(requests.get(url, params=params, timeout=TIMEOUT))
    response.response_json = response.response_json.get('data')
    response.assert_status_code(200).validate_by_schema(Company).validate_field("company_status", status.value)


@pytest.mark.parametrize("status", [status for status in Statuses])
def test_companies_limit(status):
    """
    Проверка работы параметра limit
    """
    url = API_URL_COMPANIES
    params = {
        "status": status.value,
        "limit": 1
    }
    response = Response(requests.get(url, params=params, timeout=TIMEOUT))
    response.response_json = response.response_json.get('data')
    response.assert_status_code(200).validate_by_schema(Company)
    assert len(response.response_json) <= 1, "параметр 'limit' неправильно ограничивает выдачу"
