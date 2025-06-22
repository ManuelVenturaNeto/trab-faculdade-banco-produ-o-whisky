from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base

class Destilacoes(Base):  # Fixed spelling
    __tablename__ = "destilacoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fermentacao_id = Column(Integer, ForeignKey("fermentacoes.id"), nullable=False)  # Fixed FK
    tanque_id = Column(Integer, ForeignKey("tanques.id"), nullable=False)
    vazao_id = Column(Integer, ForeignKey("vazoes.id"), nullable=False)
    teor_alcoolico_id = Column(Integer, ForeignKey("teor_alcoolicos.id"), nullable=False)
    inicio_processo = Column(DateTime, nullable=False)
    fim_processo = Column(DateTime, nullable=False)

    fermentacao = relationship("Fermentacoes", back_populates="destilacao")
    tanque = relationship("Tanques", back_populates="destilacoes")
    vazao = relationship("Vazoes", back_populates="destilacoes")
    teor_alcoolico = relationship("TeorAlcoolicos", back_populates="destilacoes")
    maturacao = relationship("Maturacoes", back_populates="destilacao")

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.fermentacao_id == other.fermentacao_id
            and self.tanque_id == other.tanque_id
            and self.vazao_id == other.vazao_id
            and self.teor_alcoolico_id == other.teor_alcoolico_id
            and self.inicio_processo == other.inicio_processo
            and self.fim_processo == other.fim_processo
        )