

from abc import ABC, abstractmethod
# from multiprocessing.connection import Client
from typing import List
from uuid import UUID
from domain.client.client_entity import Client


class ClientRepositoryInterface(ABC):
    
    @abstractmethod
    def create_client(self, client: Client) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_client(self, client_id: UUID) -> Client:
        raise NotImplementedError
    
    @abstractmethod
    def get_clients(self) -> List[Client]:
        raise NotImplementedError
    
    @abstractmethod
    def update_client(self, cliente: Client) -> Client:
        raise NotImplementedError
    
    @abstractmethod
    def delete_client(self, client_id: UUID) -> None:
        raise NotImplementedError