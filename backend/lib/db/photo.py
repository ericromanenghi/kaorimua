from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    filename = Column(String, unique=True, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    gallery_id = Column(Integer, ForeignKey('galleries.id'), nullable=False)

