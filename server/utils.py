import cv2
import os
import numpy as np
from skimage.feature import hog
from skimage import color
import joblib
import json
import io
from PIL import Image
import base64
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = os.path.join(PROJECT_ROOT, "server", "artifacts", "model.pkl")
CLASSES_PATH = os.path.join(PROJECT_ROOT, "server", "artifacts", "classes.json")

def load_model():

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
    try:
        model = joblib.load(MODEL_PATH)
        return model
    except Exception as e:
        raise ValueError(f"Failed to load model: {e}")

def load_classes():
  
    if not os.path.exists(CLASSES_PATH):
        raise FileNotFoundError(f"Classes file not found at: {CLASSES_PATH}")
    try:
        with open(CLASSES_PATH, 'r') as f:
            data = json.load(f)
        return {int(v): k for k, v in data.items()}
    except Exception as e:
        raise ValueError(f"Failed to load classes: {e}")

def convert_base64_to_image(image_base64):
    return base64.b64decode(image_base64) 

def crop_and_save_face(img_binary):
   

    img = cv2.imdecode(np.frombuffer(img_binary, np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Could not decode the image binary data.")

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_crop = img[y:y+h, x:x+w]
        face_resized = cv2.resize(face_crop, (128, 128))
        
        _, face_binary = cv2.imencode('.jpg', face_resized)
        return face_binary.tobytes()  

    print("No face detected in the image.")
    return None


def get_preprocessed_image(img_binary):

    img = cv2.imdecode(np.frombuffer(img_binary, np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Could not decode the image binary data.")


    img = cv2.resize(img, (128, 128))
    gray = color.rgb2gray(img)

    hog_feat = hog(
        gray,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        visualize=False
    )

    return np.array(hog_feat)



def classify_image(input_path):
    img_path = crop_and_save_face(input_path)
    if img_path is None:
        return {'error': 'No face detected'}
    preprocessed_image = get_preprocessed_image(img_path)
    model = load_model()
    classes = load_classes()
    prediction = model.predict(preprocessed_image.reshape(1, -1)).tolist()[0]
    confidence = np.round(model.predict_proba(preprocessed_image.reshape(1, -1)).tolist()[0][prediction]*100,2)
    data ={
        'politician_name':classes[prediction],
        'confidence':confidence
    } 
    return data



