from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from .config import settings

# Inicializa o motor (engine) do banco de dados
engine = create_engine(settings.CONEXAO_BANCO_DE_DADOS)

# Configura a fábrica de sessões do SQLAlchemy
SessaoLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos ORM herdarem
Base = declarative_base()


def obter_sessao() -> Generator[Session, None, None]:
    """Gerador que fornece uma sessão do banco de dados e garante seu fechamento."""
    banco = SessaoLocal()
    try:
        yield banco
    finally:
        banco.close()


def criar_tabelas() -> None:
    """Cria no banco de dados todas as tabelas registradas que herdam de Base."""
    Base.metadata.create_all(bind=engine)
