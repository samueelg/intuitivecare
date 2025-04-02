from pydantic import BaseModel
from datetime import date
from typing import Optional


class OperadoraAtivaSchema(BaseModel):
    reg_ans: int
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = None
    modalidade: Optional[str] = None
    logradouro: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    cep: Optional[str] = None
    ddd: Optional[str] = None
    telefone: Optional[str] = None
    fax: Optional[str] = None
    endereco_eletronico: Optional[str] = None
    representante: Optional[str] = None
    cargo_representante: Optional[str] = None
    regiao_de_comercializacao: Optional[str] = None
    data_registro_ans: Optional[date] = None

    class Config:
        from_attributes = True


class ContaContabilSchema(BaseModel):
    data: date
    reg_ans: int
    cd_conta_contabil: str
    descricao: str
    vl_saldo_inicial: float
    vl_saldo_final: float

    class Config:
        from_attributes = True


class BuscaResponseSchema(BaseModel):
    contas_contabeis: list[ContaContabilSchema]
    operadoras: list[OperadoraAtivaSchema]
