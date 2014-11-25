from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

from base import Base


class Website(Base):
    __tablename__ = "website"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    domain = Column(String)
    pages_cnt = Column(Integer)
    html_v = Column(Float)
    multi_lang = Column(Boolean)
