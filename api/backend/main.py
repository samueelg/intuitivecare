from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import search
from app.database import engine, Base

# Criar tabelas automaticamente no banco
Base.metadata.create_all(bind=engine)

# Instanciar o FastAPI
app = FastAPI(title="API de Busca com FastAPI e PostgreSQL")

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://192.168.1.15:8080"],  # Adicione todos os domínios do frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

# Registrar a rota de busca
app.include_router(search.router)

@app.get("/")
def root():
    return {"message": "API de busca está rodando!"}
