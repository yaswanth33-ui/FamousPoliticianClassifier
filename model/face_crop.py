import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


input_dir = 'dataset/train'
output_dir = 'cropped/train'


os.makedirs(output_dir, exist_ok=True)


for person in os.listdir(input_dir):
    person_input_path = os.path.join(input_dir, person)
    person_output_path = os.path.join(output_dir, person.replace(" face", ""))
    os.makedirs(person_output_path, exist_ok=True)

    for i, filename in enumerate(os.listdir(person_input_path)):
        img_path = os.path.join(person_input_path, filename)

        img = cv2.imread(img_path)
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)


        for (x, y, w, h) in faces:
            face_crop = img[y:y+h, x:x+w]
            face_resized = cv2.resize(face_crop, (128, 128))  
            out_path = os.path.join(person_output_path, f"{i}.jpg")
            cv2.imwrite(out_path, face_resized)
            break  
