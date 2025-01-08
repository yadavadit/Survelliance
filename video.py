import os
import cv2
import process

video_capture = cv2.VideoCapture(0)
process_this_frame = True

while True:
    ret, image = video_capture.read()
    save_path = os.path.join('processed/', 'tmp.jpg')
    cv2.imwrite(save_path, image)
    if process_this_frame:
        processed_image = process.process_image(save_path)
    
    process_this_frame = not process_this_frame
    cv2.imshow('Video', processed_image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
os.remove("processed/tmp.jpg")