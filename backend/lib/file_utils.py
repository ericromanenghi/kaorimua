import uuid
import os

from flask import current_app

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
    file.save(get_full_path(filename))

def get_full_path(filename):
    return os.path.join(current_app.config['UPLOAD_FOLDER'], filename)