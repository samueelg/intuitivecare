from sqlalchemy import Column, Integer, String, DECIMAL, Date, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from .database import Base

class OperadoraAtiva(Base):
    __tablename__ = "operadoras_ativas"

    reg_ans = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(18), nullable=False)
    razao_social = Column(String(255), nullable=False)
    nome_fantasia = Column(String(255))
    modalidade = Column(String(100))
    logradouro = Column(String(255))
    numero = Column(String(80))
    complemento = Column(String(100))
    bairro = Column(String(100))
    cidade = Column(String(100))
    uf = Column(CHAR(2))
    cep = Column(String(10))
    ddd = Column(CHAR(2))
    telefone = Column(String(20))
    fax = Column(String(20))
    endereco_eletronico = Column(String(255))
    representante = Column(String(255))
    cargo_representante = Column(String(100))
    regiao_de_comercializacao = Column(String(255))
    data_registro_ans = Column(Date)

    # relacionamento com cd_conta_contabil
    contas_contabeis = relationship("ContaContabil", back_populates="operadora")


class ContaContabil(Base):
    __tablename__ = "cd_conta_contabil"

    data = Column(Date, nullable=False)
    reg_ans = Column(Integer, ForeignKey("operadoras_ativas.reg_ans"), index=True)
    cd_conta_contabil = Column(String(50), primary_key=True, index=True)
    descricao = Column(String(255))
    vl_saldo_inicial = Column(DECIMAL(15, 2))
    vl_saldo_final = Column(DECIMAL(15, 2))

    # relacionamento com operadoras_ativas
    operadora = relationship("OperadoraAtiva", back_populates="contas_contabeis")
