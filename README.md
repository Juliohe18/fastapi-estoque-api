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
- Listar produtos com estoque baixo
- Listar produtos apenas pelo nome de cada produto
- Atualizar produto 
- Deletar produto

## Como executar o projeto

1. Clonar o repositório(comandos terminal)
git clone https://github.com/seu-usuario/fastapi-estoque-api.git

cd fastapi-estoque-api

2. Rodar o projeto com Docker(comando terminal)
docker compose up --build

3. Acessar a API
Após iniciar os containners, a API estará disponivel em:

http://localhost:8000

Documentação interativa:


http://localhost:8000/docs

## Endpoints da API

Produtos

POST /products/ Create Product
- Cria produtos no banco de dados

GET /products/ List
- Mostra uma lista com todos os produtos criados e suas respectivas informações

GET /products/low_stock Low Stock
- Mostra uma lista com todos os produtos abaixo do estoque minimo requisitado para cada um

GET /products/name/{product_name} List Name
- Mostra uma lista com apenas os nomes de todos os produtos cadastrados

GET /products/id/{product_id} Search
- Busca produtos cadastrados pelo seu respectivo ID

PUT /products/update/{update_product} Update
- Faz alterações nas informações de produtos cadastrados

DELETE /products/delete/{delete_product} Delete
- Deleta um produto e todas as suas informações do banco de dados através de seu respectivo ID