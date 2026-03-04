from sqlalchemy.orm import Session
from . import models, schemas


def create_product(db: Session, produto: schemas.ProdutoCreate):
    db_product = models.Product(**produto.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def list_product(db: Session, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    products =  db.query(models.Product).offset(offset).limit(per_page).all()
    
    total = db.query(models.Product). count()

    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "items": products
    } 


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


def get_low_stock_products(db: Session):
    return db.query(models.Product).filter(models.Product.quantity <= models.Product.min_stock).all()