from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from Connection import Base


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    date = Column(String)
    time = Column(String)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="projections")
