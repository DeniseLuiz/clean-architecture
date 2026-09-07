

from uuid import UUID

from src.domain.client.email_vo import Email


class Client():
    id: UUID
    name: str
    email: str
    ativo: bool = True
    
    def __init__(
        self,
        id: UUID,
        name: str,
        email: Email,
        ativo: bool):
        
        self.id = id
        self.name = name
        self.email = email
        self.ativo = ativo
    
    def __post_init__(self):
        self.validate()
    
    def validate(self):
        if not self.name or not self.name.split():
            raise ValueError('This value is required')