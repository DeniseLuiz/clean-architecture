
from uuid import UUID

from pydantic import BaseModel

class GetClientInputDTO(BaseModel):
    id: UUID
    
class GetClientOutputDTO(BaseModel):
    id: UUID
    name: str
    email: str
    active: bool