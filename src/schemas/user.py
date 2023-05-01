from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UserErrors


class User(BaseModel):
    first_name: object
    last_name: str
    company_id: object
    user_id: int

    # @validator('email')
    # def check_that_dog_presented_in_email_address(cls, email):
    #     if "@" in email:
    #         return email
    #     else:
    #         raise ValueError(UserErrors.WRONG_EMAIL.value)
