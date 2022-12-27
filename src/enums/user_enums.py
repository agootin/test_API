from enum import Enum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class UserErrors(Enum):
    WRONG_EMAIL = "email does not contain @"
