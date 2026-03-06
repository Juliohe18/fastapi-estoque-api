from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB = "postgresql+psycopg2://postgres:admin123@localhost:5432/estoque_db"

engine = create_engine(DB)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
