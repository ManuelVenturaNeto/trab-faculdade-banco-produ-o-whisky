from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class Fermentacoes(Base):  # Fixed spelling
    __tablename__ = "fermentacoes"  # Fixed table name

    id = Column(Integer, primary_key=True, autoincrement=True)
    mosturacao_id = Column(Integer, ForeignKey("mosturacoes.id"), nullable=False)
    ph_id = Column(Integer, ForeignKey("phs.id"), nullable=False)
    temperatura_id = Column(Integer, ForeignKey("temperaturas.id"), nullable=False)
    densidade_id = Column(Integer, ForeignKey("densidades.id"), nullable=False)
    tanque_id = Column(Integer, ForeignKey("tanques.id"), nullable=False)
    inicio_processo = Column(DateTime, nullable=False)
    fim_processo = Column(DateTime, nullable=False)

    mosturacao = relationship("Mosturacoes", back_populates="fermentacao")
    ph = relationship("Phs", back_populates="fermentacoes")
    temperatura = relationship("Temperaturas", back_populates="fermentacoes")
    densidade = relationship("Densidades", back_populates="fermentacoes")
    tanque = relationship("Tanques", back_populates="fermentacoes")
    destilacao = relationship("Destilacoes", back_populates="fermentacao")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.mosturacao_id == other.mosturacao_id
            and self.tanque_id == other.tanque_id
            and self.temperatura_id == other.temperatura_id
            and self.densidade_id == other.densidade_id
            and self.inicio_processo == other.inicio_processo
            and self.fim_processo == other.fim_processo
        )