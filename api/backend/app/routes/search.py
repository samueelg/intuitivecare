from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import buscar_registros
from ..schemas import BuscaResponseSchema

router = APIRouter()

@router.get("/buscar", response_model=BuscaResponseSchema)
def search(termo: str, db: Session = Depends(get_db)):
    return buscar_registros(db, termo)
