from flask import current_app
from slugify import slugify

from .db.gallery import Gallery
from .db.base import db_session
from .renders import render_photo, render_gallery
from . import photo

def add_new_gallery(gallery_name, photographer=None, model=None):
    slug = slugify(gallery_name)

    gallery = Gallery(
        name=gallery_name,
        slug=slug,
        photographer=photographer,
        model=model
    )

    db_session.add(gallery)
    db_session.commit()

    return {'gallery': render_gallery(gallery)}

def update_gallery(gallery_id, gallery_name, photographer=None, model=None):
    gallery = db_session.query(Gallery).get(gallery_id)

    if gallery is None:
        return {'error': "Gallery doesn't exist"}

    slug = slugify(gallery_name)

    gallery.name = gallery_name
    gallery.slug = slug
    gallery.photographer = photographer
    gallery.model = model

    db_session.commit()

    return {'gallery': render_gallery(gallery)}

def get_gallery(gallery_id):
    gallery = db_session.query(Gallery).get(gallery_id)

    if gallery is None:
        return {}
    
    return {'gallery': render_gallery(gallery)}

def get_all_galleries(allow_empty=0):
    if allow_empty:
        galleries = db_session.query(Gallery).all()
    else:   
        galleries = filter(lambda g: len(g.photos) > 0, db_session.query(Gallery).all())

    return {"galleries": list(map(render_gallery, galleries))}

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