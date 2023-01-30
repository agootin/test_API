from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color
from src.enums.user_enums import Statuses
from example_json import computer


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


comp = Computer.parse_obj(computer)
print(comp)
