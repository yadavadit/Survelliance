import cv2
import recognizor

video_capture = cv2.VideoCapture(0)

known_face_encodings, known_face_names = recognizor.init()

process_this_frame = True

while True:
    ret, image = video_capture.read()
    if process_this_frame:
        face_names, face_locations = recognizor.recognize(image, known_face_encodings, known_face_names)    
    
    process_this_frame = not process_this_frame
    image = recognizor.label_image(image, face_locations, face_names)
    cv2.imshow('Video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()