from faker import Faker

from src.generators.base_builder import BuilderBaseClass


class PlayerLocalizationBuilder(BuilderBaseClass):
    def __init__(self, lang):
        super().__init__()
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name()
        }

