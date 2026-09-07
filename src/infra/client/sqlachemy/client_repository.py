from sqlalchemy.orm import Session
from domain.client.client_repository_interface import ClientRepositoryInterface
from domain.client.client_entity import Client
from infra.client.sqlachemy.client_model import ClientModel
import uuid
from domain.client.email_vo import Email

class ClientRepositoryInterfaceSQLAchemy(ClientRepositoryInterface):
    session: Session
    
    def __init__(self, session: Session):
        self.session = session
    
    def create_client(self, client: Client) -> None:
        client_model = ClientModel(
            id = client.id,
            name = client.name,
            email = client.email.value,
            active = client.active     
        )
        
        self.session.add(client_model)
        self.session.commit()
    
    def get_client(self, client_id: uuid.UUID) -> Client | None:
        client_model = self.session.query(ClientModel).filter(ClientModel.id == client_id).first()
        if not client_model:
            return None
        
        return Client(
            id = client_model.id,
            name = client_model.name,
            email = Email(value = client_model.email),
            active = client_model.active
        )
