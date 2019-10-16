from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    extension = Column(String)
    gallery_id = Column(Integer, ForeignKey('galleries.id'))

