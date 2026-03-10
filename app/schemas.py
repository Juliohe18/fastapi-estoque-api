from pydantic import BaseModel
from . import main

class ProdutoBase(BaseModel):
    name: str
    quantity: int
    min_stock: int
    price: float


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoUpdate(ProdutoBase):
    pass


class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True


class PaginatedResponse(BaseModel):
    page: int
    per_page: int
    total: int
    items: list[ProdutoResponse]


class ProductNamePaginatedResponse(BaseModel):
    page: int
    per_page: int
    total: int
    items: list[str]



    

