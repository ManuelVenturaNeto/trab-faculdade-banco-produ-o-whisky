from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class Tanques(Base):
    __tablename__ = "tanques"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    tipo = Column(String(255), nullable=False)
    capacidade = Column(Integer, nullable=False)
    status_tanque = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=True)

    mosturacoes = relationship("Mosturacoes", back_populates="tanque")
    fermentacoes = relationship("Fermentacoes", back_populates="tanque")
    destilacoes = relationship("Destilacoes", back_populates="tanque")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.nome == other.nome
            and self.tipo == other.tipo
            and self.capacidade == other.capacidade
            and self.status_tanque == other.status_tanque
            and self.descricao == other.descricao
        )