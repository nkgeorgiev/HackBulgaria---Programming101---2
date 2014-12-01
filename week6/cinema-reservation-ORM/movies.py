from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from connection import Base


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

