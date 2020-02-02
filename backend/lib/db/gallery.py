from .base import Base
from .photo import Photo
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Gallery(Base):
    __tablename__ = 'galleries'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    photographer = Column(String, nullable=True)
    model = Column(String, nullable=True)
    photos = relationship(
    	"Photo",
    	order_by = Photo.id,
    	cascade = "all, delete, delete-orphan"
    )
