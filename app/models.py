from sqlalchemy import Column, String, Integer, Float
from .database import Base


class Product(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    min_stock = Column(Integer)
    price = Column(Float)


def __init__(self, name, quantity, min_stock, price):
    self.name = name
    self.quantity = quantity
    self.min_stock = min_stock
    self.price = price
