from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)

class Admin(Base):
    __tablename__ = "admin"

    username = Column(String(255), primary_key=True, index=True)
    password = Column(String(255), nullable=False)