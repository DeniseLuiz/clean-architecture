
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.client.create_client.create_client_dto import CreateClientInputDTO
from application.client.create_client.create_client_use_case import CreateClienteUseCase
from application.client.get_client.get_client_dto import GetClientInputDTO
from application.client.get_client.get_client_use_case import GetClientUseCase
from infra.api.database import obter_sessao

from infra.client.sqlachemy.client_repository import ClientRepositoryInterfaceSQLAchemy


# @router.post("/", status_code = 201)

client_router = APIRouter(prefix="/clients", tags=["Clients"])


@client_router.post("/", status_code=201)
def create_client(input: CreateClientInputDTO, session: Session = Depends(obter_sessao)):
    try:
        client_repository = ClientRepositoryInterfaceSQLAchemy(session = session)
        usecase = CreateClienteUseCase(client_repository)
        output_dto = usecase.execute(input=input)
        
    except Exception as e:
        raise HTTPException(status_code = 400, detail=str(e))
    return output_dto

@client_router.get("/{client_id}", status_code = 200)
def get_client(client_id: str, session: Session = Depends(obter_sessao)):
    try:
        client_repository = ClientRepositoryInterfaceSQLAchemy(session = session)
        usecase = GetClientUseCase(client_repository)
        output_dto = usecase.execute(input=client_id)
        if not output_dto:
            raise ('Client not found')
        return output_dto
    except Exception as e:
        raise HTTPException(status_code = 400, detail=str(e))    