from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class Mosturacoes(Base):
    __tablename__ = "mosturacoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ph_id = Column(Integer, ForeignKey("phs.id"), nullable=False)
    temperatura_id = Column(Integer, ForeignKey("temperaturas.id"), nullable=False)
    lote_ingrediente_id = Column(Integer, ForeignKey("lotes_ingredientes.id"), nullable=False)
    tanque_id = Column(Integer, ForeignKey("tanques.id"), nullable=False)
    inicio_processo = Column(DateTime, nullable=False)
    fim_processo = Column(DateTime, nullable=False)

    ph = relationship("Phs", back_populates="mosturacoes")
    temperatura = relationship("Temperaturas", back_populates="mosturacoes")
    lote_ingrediente = relationship("LoteIngredientes", back_populates="mosturacoes")
    tanque = relationship("Tanques", back_populates="mosturacoes")
    fermentacao = relationship("Fermentacoes", back_populates="mosturacao")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.ph_id == other.ph_id
            and self.temperatura_id == other.temperatura_id
            and self.lote_ingrediente_id == other.lote_ingrediente_id
            and self.tanque_id == other.tanque_id
            and self.inicio_processo == other.inicio_processo
            and self.fim_processo == other.fim_processo
        )