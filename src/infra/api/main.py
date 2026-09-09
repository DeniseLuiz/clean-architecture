from fastapi import FastAPI
# from infra.api.routers import cliente_router, pedido_router, produto_router
from infra.api.routers.client_router import client_router
from infra.api.database import criar_tabelas

app = FastAPI()

app.include_router(client_router)
# app.include_router(pedido_router.router)
# app.include_router(produto_router.router)

criar_tabelas()
