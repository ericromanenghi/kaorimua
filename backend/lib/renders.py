def render_photo(photo):
    return {
        'id': photo.id,
        'filename': photo.filename,
        'width': photo.width,
        'height': photo.height,
        'gallery_id': photo.gallery_id
    }


def render_gallery(gallery):
    return {
        'id': gallery.id,
        'name': gallery.name,
        'photos': list(map(render_photo, gallery.photos))
    }
