import pytest
import requests
from src.baseclasses.response import Response
from src.schemas.company import Company
from tests.configuration import API_URL_COMPANIES
from tests.configuration import TIMEOUT


def test_get_company_by_id():
    company_id = 1
    url = f'{API_URL_COMPANIES}/{company_id}'
    headers = {'Accept-Language': 'en'}
    response = Response(requests.get(url, headers=headers, timeout=TIMEOUT))
    response.assert_status_code(200).validate_by_schema(Company)


@pytest.mark.parametrize('company_id', [0, 2 ** 20, -1])
def test_get_not_existing_company(company_id):
    """
    Передача несуществующих company_id
    """
    url = f'{API_URL_COMPANIES}/{company_id}'
    response = Response(requests.get(url, timeout=TIMEOUT))
    response.assert_status_code(404)

