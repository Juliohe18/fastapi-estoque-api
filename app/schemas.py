from pydantic import BaseModel

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

