from pydantic import BaseModel, validator
from src.enums.global_enums import Statuses


class Company(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: Statuses

