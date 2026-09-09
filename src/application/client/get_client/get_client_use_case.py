

from application.client.get_client.get_client_dto import GetClientInputDTO, GetClientOutputDTO
from domain.__seedwork.use_case_interface import UseCaseInterface
from domain.client.client_repository_interface import ClientRepositoryInterface


class GetClientUseCase(UseCaseInterface):
    client_repository: ClientRepositoryInterface
    
    def __init__(self, client_repo):
        self.client_repository = client_repo
        
    def execute(self, input: str) -> GetClientOutputDTO:
        client = self.client_repository.get_client(input)
        
        if not client:
            raise ValueError('Client not found')

        return GetClientOutputDTO(
            id = client.id,
            name = client.name, 
            email = client.email.value,
            active = client.active
        )