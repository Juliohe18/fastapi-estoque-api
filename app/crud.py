from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def create_product(db: Session, produto: schemas.ProdutoCreate):
    existing_product = db.query(models.Product).filter(models.Product.name == produto.name).first()
    if existing_product:
        raise HTTPException(status_code=400,
                            detail="Produto já cadastrado")
    db_product = models.Product(**produto.model_dump(exclude_unset=True))
    try:
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400,
                            detail="Erro ao criar produto"
        )
    
    return db_product


def list_product(db: Session, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    query =  db.query(models.Product)
    total = query.count()
    products = query.offset(offset).limit(per_page).all()
    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "items": products
    }


def search_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(product_id == models.Product.id).first()
    return product
        


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


def get_low_stock_products(db: Session, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    total = db.query(models.Product).filter(
        models.Product.quantity <= models.Product.min_stock).count()
    products = db.query(models.Product).filter(
        models.Product.quantity <= models.Product.min_stock).offset(offset).limit(per_page)

    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "items": products
    }


def get_list_name(db: Session, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    products_name = db.query(models.Product.name).offset(offset).limit(per_page).all()
    total = db.query(models.Product.name).count()
    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "items": [p.name for p in products_name]
    }


