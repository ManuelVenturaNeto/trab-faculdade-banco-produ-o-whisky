from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class Phs(Base):
    __tablename__ = "phs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Integer, nullable=False)
    momento_leitura = Column(DateTime, nullable=False)

    mosturacoes = relationship("Mosturacoes", back_populates="ph")
    fermentacoes = relationship("Fermentacoes", back_populates="ph")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.valor == other.valor
            and self.momento_leitura == other.momento_leitura
        )