import pytest

import tables
from src.enums.user_enums import Statuses
from example_json import computer
from src.schemas.computer import Computer
from src.generators.person_builder import PersonBuilder


@pytest.mark.parametrize("status", [status.value for status in Statuses])
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).update_inner_value(["localize", "en", "new_value"], "asd").build())


def test_pydantic_object():
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.physical)


# def test_delete_from_db(get_db_session, get_delete_method):
#     table = tables.Person
#     get_delete_method(get_db_session, table, table.person_id == 4)
#     assert get_db_session.query(table).filter(table.person_id == 4).one_or_none() is None, "row is still present in DB"
#
#
# def test_add_to_db(get_db_session, get_add_to_db_method):
#     table = tables.Person
#     new_person = PersonBuilder().build()
#     new_person_db_object = table(person_id=999999997, person_name=new_person["name"])
#     get_add_to_db_method(get_db_session, new_person_db_object)
#     assert get_db_session.query(table).filter(table.person_id == 999999997).one_or_none(), "no new person in DB"
