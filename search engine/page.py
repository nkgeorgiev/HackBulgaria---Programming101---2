from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from base import Base




class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    website_id = Column(Integer, ForeignKey("website.id"))
    website = relationship("Website", backref="pages")
    url = Column(String)
    title = Column(String)
    desc = Column(String)
    ads = Column(Integer)
    ssl = Column(Boolean)
    points = Column(Float)

