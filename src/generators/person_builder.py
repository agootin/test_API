from src.generators.base_builder import BuilderBaseClass

from faker import Faker


class PersonBuilder(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.set_person_name()

    def set_person_name(self):
        self.result["name"] = Faker("en_US").name()
        return self


print(PersonBuilder().build())
