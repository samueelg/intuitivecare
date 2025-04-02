
# API de Busca com FastAPI e Vue.js

## Descrição

Este projeto consiste em uma API de busca desenvolvida com FastAPI e um frontend utilizando Vue.js. A API busca e retorna informações de contas contábeis e operadoras de planos de saúde. O frontend permite a pesquisa dessas informações e exibe os resultados de forma organizada utilizando DataTable.

## Tecnologias Utilizadas
* **Backend:** FastAPI, PostgreSQL
* **Frontend:** Vue.js, Axios

## Requisitos para iniciar o projeto

* Ter criado o banco de dados com as tabelas e seus inserido os seus respectivos dados das Operadoras Ativas, e das Contas Contabeis.

## Como Executar o Projeto

### 1. Clone o repositorio e acesse o diretorio da API

```bash 
git clone https://github.com/samueelg/intuitivecare.git
cd intuitivecare/api
```

### 2. Configurar o Backend
#### 2.1 Instalar as dependencias
Instale as dependencias para rodar o projeto seguindo os seguintes comandos: 

```bash 
pip install fastapi
pip install sqlalchemy
pip install dotenv
```

#### 2.2 Configurar a conexão com o Banco de Dados
Configure a conexão com o banco de dados no arquivo ```.env```
```bash
postgresql://usuario:senha@localhost:5432/nomedobanco
```

#### 2.3 Rodar a API
No terminal do VS Code, inicie a API com o comando:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Configurar o Frontend

#### 3.1 Instalar Dependências
```bash 
cd frontend
pip install axios
```

#### 3.2 Configurar a Base URL

No arquivo ```api.js```, configure a ```baseURL``` para apontar para a API FastAPI:

```bash 
const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});
```
#### 3.3 Rodar o Frontend
No terminal do VS Code, crie mais um terminal e inicie a aplicação do frontend com o comando:
```bash 
npm run serve
```
