from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    filename = Column(String, unique=True)
    width = Column(Integer)
    height = Column(Integer)
    gallery_id = Column(Integer, ForeignKey('galleries.id'))

