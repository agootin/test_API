from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization


class Player:

    def __init__(self):
        self.result = {}
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
                "en": PlayerLocalization("en_US").build(),
                "ru": PlayerLocalization("ru_RU").build()
            }

    def build(self):
        return self.result


z = Player().build()
print(z)
