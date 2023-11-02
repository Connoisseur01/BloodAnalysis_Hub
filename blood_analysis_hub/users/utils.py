import os
import secrets
from . import app

def save_picture(form_picture):
    random_name = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_name + file_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn