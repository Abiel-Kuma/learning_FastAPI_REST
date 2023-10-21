from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from database import conn_db

metadata = conn_db.metadata
engine = conn_db.engine
base = declarative_base()

class User(base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255))

base.metadata.create_all(engine)