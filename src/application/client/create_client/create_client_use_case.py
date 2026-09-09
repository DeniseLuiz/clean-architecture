
import uuid
# from multiprocessing.connection import Client

from application.client.create_client.create_client_dto import CreateClientInputDTO, CreateClienteOutputDTO
from domain.__seedwork import use_case_interface
from domain.client.client_repository_interface import ClientRepositoryInterface
from domain.client.email_vo import Email
from domain.client.client_entity import Client


class CreateClienteUseCase(use_case_interface.UseCaseInterface):
    client_repository: ClientRepositoryInterface
    
    def __init__(self, client_repo: ClientRepositoryInterface):
        self.client_repository = client_repo
        
    def execute(self, input: CreateClientInputDTO) -> CreateClienteOutputDTO:
        client = Client (
            id = uuid.uuid4(),
            name = input.name,
            email = Email(value = input.email),
            active = True
        )
        self.client_repository.create_client(client = client)
        
        return CreateClienteOutputDTO(
            id = client.id,
            name = client.name,
            email = client.email.value,
            active = client.active,
        )

