import os

import cv2
import numpy as np
import face_recognition
import urllib.request
from flask import Flask, request
from application import test

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():
    json = request.get_json()
    return test('ngu')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', default=8081))
