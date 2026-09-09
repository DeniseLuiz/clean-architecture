

from uuid import UUID

from domain.client.email_vo import Email


class Client():
    id: UUID
    name: str
    email: Email
    active: bool = True
    
    def __init__(
        self,
        id: UUID,
        name: str,
        email: Email,
        active: bool
        ):
        
        self.id = id
        self.name = name
        self.email = email
        self.active = active
    
    def __post_init__(self):
        self.validate()
    
    def validate(self):
        if not self.name or not self.name.split():
            raise ValueError('This value is required')