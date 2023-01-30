from src.enums.user_enums import Statuses
from src.generators.base_builder import BuilderBaseClass
from src.generators.player_localization_builder import PlayerLocalizationBuilder


class PlayerBuilder(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.set_default_player()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="https://www.google.com/"):
        self.result["avatar"] = avatar
        return self

    def set_default_player(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
                "en": PlayerLocalizationBuilder("en_US").build(),
                "ru": PlayerLocalizationBuilder("ru_RU").build()
            }

