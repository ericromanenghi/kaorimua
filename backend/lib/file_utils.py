import uuid
import os

from flask import current_app
from PIL import Image

MAX_HEIGHT = 1200

def allowed_extensions():
    return current_app.config['ALLOWED_EXTENSIONS']

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()

def allowed_file(filename):
    if '.' not in filename:
        return False

    return get_file_extension(filename) in allowed_extensions()

def secure_filename(filename):
    extension = get_file_extension(filename)

    return '.'.join([str(uuid.uuid4()), extension])

def save_file(file, filename):
    full_path = get_full_path(filename)
    file.save(full_path)
    try:
        resize_image(full_path)
    except:
        current_app.logger.error("Image couldn't be resized")

def get_full_path(filename):
    return os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

def resize_image(filename):
    img = Image.open(filename)
    (width, height) = img.size
    if height > MAX_HEIGHT:
        ratio = width / height
        new_size = (round(MAX_HEIGHT * ratio), MAX_HEIGHT)
        new_img = img.resize(new_size, Image.LANCZOS)
        new_img.save(filename)
