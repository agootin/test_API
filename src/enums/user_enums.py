from enum import Enum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class UserErrors(Enum):
    WRONG_EMAIL = "email does not contain @"
