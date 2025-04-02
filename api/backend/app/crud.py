from sqlalchemy.orm import Session
from .models import ContaContabil, OperadoraAtiva


def buscar_registros(db: Session, termo: str):

    # Busca nas contas contábeis pelo campo 'descricao'
    contas_contabeis = (
        db.query(ContaContabil)
        .filter(ContaContabil.descricao.ilike(f"%{termo}%"))
        .all()
    )

    # Busca nas operadoras pelo campo 'razao_social'
    operadoras = (
        db.query(OperadoraAtiva)
        .filter(OperadoraAtiva.razao_social.ilike(f"%{termo}%"))
        .all()
    )

    return {"contas_contabeis": contas_contabeis, "operadoras": operadoras}
