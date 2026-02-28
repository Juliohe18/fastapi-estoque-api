from sqlalchemy.orm import Session
from . import models, schemas

def create_product(db: Session, produto: schemas.ProdutoCreate):
    db_product = models.Product(**produto.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def list_product(db: Session):
    return db.query(models.Product).all()


def search_product(db: Session, product_id: int):
    return db.query(models.Product).filter(product_id == models.Product.id).first()


def update_product(db: Session, product_id: int, product: schemas.ProdutoUpdate):
    db_product = search_product(db, product_id)
    if db_product:
        for key, value in product.model_dump().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = search_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
