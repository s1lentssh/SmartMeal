import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE_URL = f"sqlite:///{os.environ.get('DB_LOCATION')}"

engine = sa.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sa.orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
