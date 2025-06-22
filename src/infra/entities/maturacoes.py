from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class Maturacoes(Base):
    __tablename__ = "maturacoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    destilacao_id = Column(Integer, ForeignKey("destilacoes.id"), nullable=False)  # Fixed FK
    inicio_processo = Column(DateTime, nullable=False)
    fim_processo = Column(DateTime, nullable=False)

    destilacao = relationship("Destilacoes", back_populates="maturacao")
    empacotamento = relationship("Empacotamentos", back_populates="maturacao")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.destilacao_id == other.destilacao_id
            and self.inicio_processo == other.inicio_processo
            and self.fim_processo == other.fim_processo
        )