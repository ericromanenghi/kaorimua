from flask import current_app
from .db.gallery import Gallery
from .db.base import db_session
from .renders import render_photo, render_gallery
from . import photo

def add_new_gallery(gallery_name):
    gallery = Gallery(name=gallery_name)

    db_session.add(gallery)
    db_session.commit()

    return {'gallery': render_gallery(gallery)}

def get_gallery(gallery_id):
    gallery = db_session.query(Gallery).get(gallery_id)

    if gallery is None:
        return {}
    
    return {'gallery': render_gallery(gallery)}

def get_all_galleries():
    return {"galleries": list(map(render_gallery, db_session.query(Gallery).all()))}

def delete_gallery(gallery_id):
    gallery = db_session.query(Gallery).get(gallery_id)

    deleted = 0

    if gallery is None:
        current_app.logger.debug(f'Tried to delete unexisting gallery')
        return {'deleted': deleted}

    try:
        db_session.delete(gallery)
        db_session.commit()
        deleted = 1
    except:
        current_app.logger.error(f'Could not delete gallery {gallery.id}')

    return {'deleted': deleted}

def get_gallery_photos(gallery_id):
    return photo.get_by_gallery_id(gallery_id)