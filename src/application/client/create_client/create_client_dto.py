

from uuid import UUID

from pydantic import BaseModel


class CreateClientInputDTO(BaseModel):
    name: str
    email: str

class CreateClienteOutputDTO(BaseModel):
    id: UUID
    name: str
    email: str
    active: bool