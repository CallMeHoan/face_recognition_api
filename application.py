
# urlBill = 'https://scontent.fsgn5-9.fna.fbcdn.net/v/t1.6435-9/133480305_1025775777934271_8384115018610540736_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=174925&_nc_ohc=lqx6Uuk6gsoAX93OULq&_nc_ht=scontent.fsgn5-9.fna&oh=00_AfCTQssmh_T6-cMDuwLixudGLHWGRR8hG-uU2gAZufUUkw&oe=64CBD82D'
# responseBill = urllib.request.urlopen(urlBill)
# imgBill = face_recognition.load_image_file(responseBill)
# imgBill = cv2.cvtColor(imgBill, cv2.COLOR_BGR2RGB)
# cv2.imshow('Bill', imgBill)
#
# urlTest = 'https://media.wired.com/photos/649c76576279e36472844646/master/w_2560%2Cc_limit/Elon-Musk-Vivatech-Business-1499013102.jpg'
# responseTest = urllib.request.urlopen(urlTest)
# imgTest = face_recognition.load_image_file(responseTest)
# imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
#
# try:
#     faceLoc = face_recognition.face_locations(imgBill)[0]
#     encodeBill = face_recognition.face_encodings(imgBill)[0]
#     cv2.rectangle(imgBill, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
#
#     faceLogTest = face_recognition.face_locations(imgTest)[0]
#     encodeTest = face_recognition.face_encodings(imgTest)[0]
#     cv2.rectangle(imgTest, (faceLogTest[3], faceLogTest[0]), (faceLogTest[1], faceLogTest[2]), (255, 0, 255), 2)
#
#     results = face_recognition.compare_faces([encodeBill], encodeTest, 0.6)
#     print(results)
# except IndexError:
#     print("ngu")
#
# cv2.imshow('Bill', imgBill)
# cv2.imshow('test', imgTest)
# cv2.waitKey(0)
def test(name):
    return 'hello' + name