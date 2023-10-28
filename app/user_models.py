from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
import uuid
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(255), unique=True, nullable=True)
    password = Column(String(100))
    is_admin = Column(Boolean, default=False)