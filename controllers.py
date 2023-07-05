import os
from flask import Flask, request
from application import *

app = Flask(__name__)


@app.route('/check/images', methods=['POST'])
def check_images():
    try:
        json_data = request.get_json()
        if not json_data:
            return response(-9999, 'failed', 'missing_params')

        images_urls = json_data.get('image_urls')
        return face_detect_from_images(images_urls)
    except AttributeError as e:
        return response(-9999, 'failed', str(e))


@app.route('/check/face_recognition', methods=['POST'])
def face_compare():
    try:
        json_data = request.get_json()
        if not json_data:
            return response(-9999, 'failed', 'missing_params')

        image_urls = json_data.get('image_urls')
        defined_image = json_data.get('defined_image')
        return face_compare(image_urls, defined_image)
    except AttributeError as e:
        return response(-9999, 'failed', str(e))


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', default=8081))
