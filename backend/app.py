import json

from flask import Flask, request, Response
from flask_cors import CORS

from sqlalchemy.exc import IntegrityError

app = Flask(__name__, instance_relative_config=True)
CORS(app)

app.config.from_object('config.default')
app.config.from_pyfile('config.py', silent=True)
app.config.from_envvar('CONFIG_FILE')
app.config['CORS_HEADERS'] = 'Content-Type'

with app.app_context():
    from lib import db, gallery, photo, file_utils

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.base.db_session.remove()


@app.route('/')
def index():
    return Response(json.dumps({"api_version": "API kaorimua.nl/v0.1"}), mimetype='application/json')


@app.route('/photo', methods=['POST'])
def process_photo_request():
    files = request.files

    if 'gallery_id' not in request.form:
        return 'Gallery id is required', 400

    gallery_id = request.form['gallery_id']

    if 'file' not in request.files:
        return 'At least one file required', 400

    file = request.files['file']
    
    if not file or file.filename == '':
        return 'At least one file required', 400

    if not file_utils.allowed_file(file.filename):
        return 'File extension not allowed', 400

    filename = file_utils.secure_filename(file.filename)

    try:
        file_utils.save_file(file, filename)
        photo.add_new_photo(filename, gallery_id)
    except:
        app.logger.error("File couldn't be saved")
        return "File couldn't be saved", 500

    return Response(json.dumps({'filename': filename}), mimetype='application/json')


@app.route('/photo/<photo_id>', methods=['GET'])
def get_photo_by_id(photo_id):
    if photo_id == 'all':
        return Response(json.dumps(photo.get_all_photos()), mimetype='application/json')
    else:
        return Response(json.dumps(photo.get_photo(photo_id)), mimetype='application/json')

@app.route('/photo/<photo_id>', methods=['DELETE'])
def delete_photo(photo_id):
    return Response(json.dumps(photo.delete_photo(photo_id)), mimetype='application/json')

@app.route('/gallery', methods=['POST'])
def create_gallery():
    params = request.get_json()
    if 'gallery_name' not in params:
        return 'bad request!', 400

    gallery_name = params['gallery_name']

    try:
        response = gallery.add_new_gallery(gallery_name)
    except IntegrityError as e:
        return 'Something went wrong. It seems like you chose an already existing gallery name, please try with another one.', 500
    return Response(json.dumps(response), mimetype='application/json')

@app.route('/gallery/<gallery_id>', methods=['DELETE'])
def delete_gallery(gallery_id):
    return Response(json.dumps(gallery.delete_gallery(gallery_id)), mimetype='application/json')

@app.route('/gallery/<gallery_id>', methods=['GET'])
def get_gallery_by_id(gallery_id):
    if gallery_id == 'all':
        return Response(json.dumps(gallery.get_all_galleries()), mimetype='application/json')
    else:
        return Response(json.dumps(gallery.get_gallery(gallery_id)), mimetype='application/json')

@app.route('/gallery/<gallery_id>/photos', methods=['GET'])
def get_photos_by_gallery_id(gallery_id):
    return Response(json.dumps(gallery.get_gallery_photos(gallery_id)), mimetype='application/json')


if __name__ == '__main__':
    db.init_db()
    app.run('0.0.0.0')

