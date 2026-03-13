from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB = "postgresql://postgres:595690@db:5432/estoque_db"

engine = create_engine(DB, client_encoding="utf8")


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
