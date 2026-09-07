from infra.api.database import Base
from sqlalchemy import Column, String, Boolean

from sqlalchemy.dialects.postgresql import UUID

class ClientModel(Base):
    __tablename__ = 'tb_clients'
    
    id = Column(UUID, primary_key = True)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False)
    active = Column(Boolean, nullable = False)
    