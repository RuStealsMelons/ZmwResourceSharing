from flask import Blueprint, request, make_response
from datetime import datetime

from models.imgs import save_img, load_img

imgs = Blueprint('imgs', __name__)

@imgs.route('/uploader', methods=['POST'])
def uploader():
    file = request.files.get("img")
    if file is None:
        file = request.files.get("file")
    name = datetime.now().strftime("%Y%m%d%H%M%S") + file.filename
    save_img(name=name, data=file.read())
    return {
        "errno": 0,
        "data": {
            "url": "/api/loader/"+name,
        }
    }


@imgs.route('/loader/<img_name>', methods=['GET'])
def loader(img_name):
    print(img_name)
    if img_name is None or img_name == "":
        return "no"
    else:
        response = make_response(load_img(img_name))
        response.headers.set('Content-Type', 'image/jpeg')
        response.headers.set('Content-Disposition', 'inline', filename='image.jpg')
        return response





