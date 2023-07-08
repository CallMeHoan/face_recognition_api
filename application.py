import array as arr
import urllib.request
import cv2

import face_recognition
from response import *


def test(name):
    return 'hello' + name


# face detection function
def face_detect_from_images(image_urls: arr):
    # ảnh có 1 khuôn mặt
    acceptable_images = []
    # ảnh có 2 khuôn mặt trở lên
    unacceptable_images = []

    if len(image_urls) == 0:
        return response(-9999, 'failed', 'Không tìm thấy ảnh nào')
    for image_url in image_urls:
        response_img = urllib.request.urlopen(image_url)
        face_img = face_recognition.load_image_file(response_img)
        face_locations = face_recognition.face_locations(face_img)
        total_faces = len(face_locations)
        if total_faces == 1:
            acceptable_images.append(image_url)
        else:
            unacceptable_images.append(image_url)

    payload = {
        'acceptable_images': acceptable_images,
        'unacceptable_images': unacceptable_images
    }

    return response(9999, 'success', payload)


def face_compare(image_urls: arr, defined_image: str):
    if len(image_urls) == 0:
        return response(-9999, 'failed', 'Không có ảnh mẫu nào')
    if defined_image is None or len(defined_image) == 0:
        return response(-9999, 'failed', 'Không có ảnh để so sánh')

    encode_defined = []
    for image in image_urls:
        response_img = urllib.request.urlopen(image)
        img = face_recognition.load_image_file(response_img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        try:
            encode = face_recognition.face_encodings(img)[0]
            encode_defined.append(encode)
        except:
            print("image error " + img)

    if len(encode_defined) == 0:
        return response(-9999, 'failed', 'Ảnh mẫu bị lỗi vui lòng thay đổi ảnh mẫu')

    #
    response_defined_img = urllib.request.urlopen(defined_image)
    def_img = face_recognition.load_image_file(response_defined_img)
    def_img = cv2.cvtColor(def_img, cv2.COLOR_BGR2RGB)
    try:
        encode_defined_img = face_recognition.face_encodings(def_img)[0]
    except:
        return response(-9999, 'failed', 'Ảnh chấm công bị lỗi vui lòng thay đổi ảnh chấm công')

    results = face_recognition.compare_faces(encode_defined, encode_defined_img, 0.6)
    true = results.count(True)
    if true / len(results) > 0.6:
        return response(9999, 'success', True)
    else:
        return response(9999, 'success', False)


