import os
import cv2
from ultralytics import YOLO

def detect(file):
    model = YOLO("model_weights/weapons_yolov8.pt")
    results = model(file)
    object_names = results[0].names
    detections = []
    for result in results[0].boxes:
        cat = result.cls.item()
        cat_name = object_names[cat]
        conf = result.conf.item()    
        x1, y1, x2, y2 = result.xyxy[0].numpy() 
        detections.append((cat_name, conf, x1, y1, x2, y2))
    return detections

def label_image(image, detections, threshold=0.5):
    for (cat_name, conf, x1, y1, x2, y2) in detections:
        if conf >= threshold:
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
            cv2.rectangle(image, (int(x1), int(y2) - 35), (int(x2), int(y2)), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            label = f"{cat_name}: {conf:.2f}"
            cv2.putText(image, label, (int(x1) + 6, int(y2) - 6), font, 1.0, (255, 255, 255), 1)
    return image

def main():
    image_file = "knife.jpg"
    image_path = os.path.join('input/', image_file)
    image = cv2.imread(image_path)
    detections = detect(image_path)
    image = label_image(image, detections)
    save_path = os.path.join('processed/', 'weapon_detected_'+image_file)
    cv2.imwrite(save_path, image)

if __name__ == "__main__":
    main()


