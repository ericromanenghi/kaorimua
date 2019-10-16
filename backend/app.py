from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__, instance_relative_config=True)
CORS(app)

app.config.from_object('config.default')
app.config.from_pyfile('config.py', silent=True)
app.config.from_envvar('CONFIG_FILE')
app.config['CORS_HEADERS'] = 'Content-Type'

with app.app_context():
    from lib import db, gallery, photo

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.base.db_session.remove()


@app.route('/')
def index():
    return json.dumps({"api_version": "API kaorimua.nl/v0.1"})


@app.route('/photo', methods=['POST'])
def process_photo_request():
    params = request.get_json()
    app.logger.debug(json.dumps(params))
    if 'file_name' not in params or 'gallery_id' not in params:
        return 'bad request!', 400
    file_name = params['file_name']
    gallery_id = params['gallery_id']
    response = photo.add_new_photo(file_name, gallery_id)
    return json.dumps(response)

@app.route('/photo/<photo_id>', methods=['GET'])
def get_photo_by_id(photo_id):
    if photo_id == 'all':
        return json.dumps(photo.get_all_photos())
    else:
        return json.dumps(photo.get_photo(photo_id))

@app.route('/photo/<photo_id>', methods=['DELETE'])
def delete_photo(photo_id):
    return json.dumps(photo.delete_photo(photo_id))

@app.route('/gallery', methods=['POST'])
def create_gallery():
    params = request.get_json()
    if 'gallery_name' not in params:
        return 'bad request!', 400
    gallery_name = params['gallery_name']
    response = gallery.add_new_gallery(gallery_name)
    return json.dumps(response)

@app.route('/gallery/<gallery_id>', methods=['DELETE'])
def delete_gallery(gallery_id):
    return json.dumps(gallery.delete_gallery(gallery_id))

@app.route('/gallery/<gallery_id>', methods=['GET'])
def get_gallery_by_id(gallery_id):
    if gallery_id == 'all':
        return json.dumps(gallery.get_all_galleries())
    else:
        return json.dumps(gallery.get_gallery(gallery_id))


if __name__ == '__main__':
    db.init_db()
    app.run('0.0.0.0')

