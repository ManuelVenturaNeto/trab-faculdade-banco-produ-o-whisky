from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class TeorAlcoolicos(Base):
    __tablename__ = "teor_alcoolicos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Integer, nullable=False)
    momento_leitura = Column(DateTime, nullable=False)  # Fixed data type

    destilacoes = relationship("Destilacoes", back_populates="teor_alcoolico")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.valor == other.valor
            and self.momento_leitura == other.momento_leitura
        )