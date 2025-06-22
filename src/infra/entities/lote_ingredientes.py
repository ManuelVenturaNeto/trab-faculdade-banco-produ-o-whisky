from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class LoteIngredientes(Base):
    __tablename__ = "lotes_ingredientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ingrediente_id = Column(Integer, ForeignKey("ingredientes.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    unidade = Column(String(50), nullable=False)
    data_recebimento = Column(DateTime, nullable=False)

    ingrediente = relationship("Ingredientes", back_populates="lotes_ingredientes")
    mosturacoes = relationship("Mosturacoes", back_populates="lote_ingrediente")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.ingrediente_id == other.ingrediente_id
            and self.quantidade == other.quantidade
            and self.unidade == other.unidade
            and self.data_recebimento == other.data_recebimento
        )