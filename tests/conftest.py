import pytest
from src.generators.player_builder import PlayerBuilder

from db import Session


@pytest.fixture
def get_player_generator():
    return PlayerBuilder()


@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_test_data_from_db(session, table, filter_data):
    session.query(table).filter(filter_data).delete()
    session.commit()


def add_to_db(session, item):
    session.add(item)
    session.commit()


@pytest.fixture
def get_add_to_db_method():
    return add_to_db


@pytest.fixture
def get_delete_method():
    return delete_test_data_from_db
