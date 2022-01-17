import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./database.db"
engine = sa.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sa.orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
