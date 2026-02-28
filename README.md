# API de controle de estoque

API REST desenvolvida com FastAPI e PostgreSQL para gerenciamento de produtos.

# Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker

## Funcionalidades

- Criar produto 
- Listar Produto
- Buscar produto por ID
- Atualizar produto 
- Deletar produto

## Rodando com Docker (PostgreSQL)

'''bash
docker run --name meu-postgres \
-e POSTGRES_PASSWORD=admin123 \
-e POSTGRES_DB=estoque_db \
-p 5432:5432 \
-D postgres
'''
## Rodar aplicação

'''bash
uvicorn app.main:app --reload
'''
Acesse:
http://127.0.0.1:8000/docs
