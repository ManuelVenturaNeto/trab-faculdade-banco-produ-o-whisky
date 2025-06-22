from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class Ingredientes(Base):
    __tablename__ = "ingredientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    tipo = Column(String(255), nullable=False)
    fornecedor = Column(String(255), nullable=False)
    validade = Column(Date, nullable=False)

    lotes_ingredientes = relationship("LoteIngredientes", back_populates="ingrediente")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.nome == other.nome
            and self.tipo == other.tipo
            and self.fornecedor == other.fornecedor
            and self.validade == other.validade
        )