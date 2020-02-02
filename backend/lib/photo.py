from flask import current_app

from PIL import Image

from .db.photo import Photo
from .db.base import db_session
from .renders import render_photo
from .file_utils import get_full_path

def add_new_photo(filename, gallery_id):
    width, height = _get_photo_size(filename)

    photo = Photo(
        filename=filename,
        width=width,
        height=height,
        gallery_id=gallery_id
    )

    db_session.add(photo)
    db_session.commit()

    return {"photo": render_photo(photo)}

def get_photo(photo_id):
    photo = db_session.query(Photo).get(photo_id)

    if photo is None:
        return {}
    
    return {'photo': render_photo(photo)}

def get_all_photos():
    return {"photos": list(map(render_photo, db_session.query(Photo).all()))}

def delete_photo(photo_id):
    photo = db_session.query(Photo).get(photo_id)

    deleted = 0

    if photo is None:
        current_app.logger.debug(f'Tried to delete unexisting gallery')
        return {'deleted': deleted}

    try:
        db_session.delete(photo)
        db_session.commit()
        deleted = 1
    except:
        current_app.logger.error(f'Could not delete gallery {photo.id}')

    return {'deleted': deleted}

def get_by_gallery_id(gallery_id):
    return {
        "photos": list(map(
            render_photo,
            db_session.query(Photo).filter_by(gallery_id=gallery_id)
    ))}

def _get_photo_size(filename):
    img = Image.open(get_full_path(filename))
    return img.size
