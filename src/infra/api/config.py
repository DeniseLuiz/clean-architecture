from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    CONEXAO_BANCO_DE_DADOS: str = Field(..., env="CONEXAO_BANCO_DE_DADOS")


settings = Settings()
