import os
import face_recognition
import cv2
from utils import *

video_capture = cv2.VideoCapture(0)

face_folder = os.listdir('known_face/')
known_face_names = []
known_face_encodings = []

for index, img_file in enumerate(face_folder):
    file_path = os.path.join('known_face/', img_file)
    image  = face_recognition.load_image_file(file_path)
    known_face_encodings.append(face_recognition.face_encodings(image)[0])
    known_face_names.append(os.path.splitext(img_file)[0]) 

process_this_frame = True

while True:
    ret, image = video_capture.read()
    if process_this_frame:
        face_locations = detect_face(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        face_names = recognize_face(image, face_encodings, known_face_encodings, known_face_names)
    
    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()