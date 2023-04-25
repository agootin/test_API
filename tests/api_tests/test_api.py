import pytest
import requests
from src.baseclasses.response import Response
from src.enums.global_enums import Statuses
from src.schemas.company import Company
from tests.configuration import API_URL_COMPANIES


def test_companies():
    url = API_URL_COMPANIES
    response = requests.get(url)
    Response(response).assert_status_code(200).validate_by_schema(Company)


@pytest.mark.parametrize("status", [status for status in Statuses])
def test_companies_filtering_by_status(status):
    url = API_URL_COMPANIES
    response = requests.get(url, params="status=" + status.value)
    Response(response).assert_status_code(200).validate_by_schema(Company).validate_field("company_status", status.value)




