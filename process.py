import os
import detector
import recognizor
import cv2

def inside_screen(face_box, obj_box):
    face_top, face_right, face_bottom, face_left = face_box
    obj_x1, obj_y1, obj_x2, obj_y2 = obj_box
    if (face_left < obj_x2 and face_right > obj_x1 and face_top < obj_y2 and face_bottom > obj_y1):
        return True
    return False

def screenface(face_locations, detections):
    screen_face_list = []
    for face_box in face_locations:
        face_found_in_screen = False  
        for obj_class, _, obj_x1, obj_y1, obj_x2, obj_y2 in detections:
            if obj_class in ['cell phone', 'laptop']:  
                if inside_screen(face_box, (obj_x1, obj_y1, obj_x2, obj_y2)):
                    face_found_in_screen = True
                    break  
        screen_face_list.append(face_found_in_screen)
    return screen_face_list

def is_inside(inner, outer):
    x1_inner, y1_inner, x2_inner, y2_inner = inner
    x1_outer, y1_outer, x2_outer, y2_outer = outer
    return x1_inner > x1_outer and y1_inner > y1_outer and x2_inner < x2_outer and y2_inner < y2_outer

def process_image(image_file, input_dir='input/', output_dir='processed/'):
    image_path = os.path.join(input_dir, image_file)
    save_path = os.path.join(output_dir, 'processed_' + image_file)
    
    image = cv2.imread(image_path)

    known_face_encodings, known_face_names = recognizor.init()
    face_names, face_locations = recognizor.recognize(image, known_face_encodings, known_face_names)
    detections = detector.detect(image_path)
    
    objects_of_interest = ['cell phone', 'laptop']
    screen_bboxes = [
        (obj[2], obj[3], obj[4], obj[5])  
        for obj in detections if obj[0] in objects_of_interest
    ]
    
    screen_face_list = screenface(face_locations, detections)
    filtered_face_names = [name for name, is_in_screen in zip(face_names, screen_face_list) if not is_in_screen]
    filtered_face_locations = [loc for loc, is_in_screen in zip(face_locations, screen_face_list) if not is_in_screen]
    
    filtered_detections = [
        detection for detection in detections
        if not any(is_inside((detection[2], detection[3], detection[4], detection[5]), screen_bbox)
               for screen_bbox in screen_bboxes)
    ]
    
    image = recognizor.label_image(image, filtered_face_locations, filtered_face_names)
    image = detector.label_image(image, filtered_detections)
    cv2.imwrite(save_path, image)
    
    return save_path

def main():
    image_file = "screen_face.jpg"
    try:
        processed_path = process_image(image_file)
        print(f"Image processed successfully. Saved to: {processed_path}")
    except Exception as e:
        print(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main()