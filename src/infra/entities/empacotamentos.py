from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class Empacotamentos(Base):
    __tablename__ = "empacotamentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    maturacao_id = Column(Integer, ForeignKey("maturacoes.id"), nullable=False)
    data_empacotamento = Column(DateTime, nullable=False)
    tipo_garrafa = Column(String(100), nullable=False)
    litros_garrafa = Column(Integer, nullable=False)
    lote = Column(Integer, nullable=False)

    maturacao = relationship("Maturacoes", back_populates="empacotamento")  # Added relationship

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.maturacao_id == other.maturacao_id
            and self.data_empacotamento == other.data_empacotamento
            and self.tipo_garrafa == other.tipo_garrafa
            and self.litros_garrafa == other.litros_garrafa
            and self.lote == other.lote
        )