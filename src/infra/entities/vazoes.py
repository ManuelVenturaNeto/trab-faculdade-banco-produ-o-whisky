from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class Vazoes(Base):
    __tablename__ = "vazoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Integer, nullable=False)
    momento_leitura = Column(DateTime, nullable=False)
    tipo = Column(String(50), nullable=False)

    destilacoes = relationship("Destilacoes", back_populates="vazao")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.valor == other.valor
            and self.momento_leitura == other.momento_leitura
            and self.tipo == other.tipo
        )