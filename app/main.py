from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import session
from .database import engine, SessionLocal
from . import models, schemas, crud
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


@app.post("/products/", response_model=schemas.ProdutoResponse)
def create_product(product: schemas.ProdutoCreate, db: session = Depends(get_db)):
    return crud.create_product(db, product)


@app.get("/products/", response_model=schemas.PaginatedResponse)
def list(db: session = Depends(get_db), page: int = Query(1, ge=1), per_page: int = Query(10, ge=1, le=100)):
    return crud.list_product(db, page, per_page)


@app.get("/products/low_stock", response_model=schemas.PaginatedResponse)
def low_stock(db: session = Depends(get_db), page: int = Query(1, ge=1), per_page: int = Query(10, ge=1, le=100)):
    return crud.get_low_stock_products(db, page, per_page)


@app.get("/products/{id}", response_model=schemas.ProdutoResponse)
def search(product_id: int, db: session = Depends(get_db)):
    product = crud.search_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product


@app.put("/products/{id}", response_model=schemas.ProdutoResponse)
def update(product_id: int, product: schemas.ProdutoUpdate, db: session = Depends(get_db)):
    updated_product = crud.update_product(db, product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated_product


@app.delete("/products/{id}")
def delete(product_id: int, db: session = Depends(get_db)):
    product = crud.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"mensagem": "Produto deletado com sucesso"}
