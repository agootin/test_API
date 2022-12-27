import pytest

from src.enums.user_enums import Statuses


@pytest.mark.parametrize("status", [status.value for status in Statuses])
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).build())

