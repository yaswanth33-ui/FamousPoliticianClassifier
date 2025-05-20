import numpy as np 
import os
from skimage.feature import hog, local_binary_pattern
from skimage import color
import cv2
from sklearn.preprocessing import LabelEncoder

'''def extract_combined_features(image):
    hog_feat = hog(image,pixels_per_cell=(8,8),cells_per_block=(2,2),visualize=False)
    
    lbp = local_binary_pattern(image, 8, 1, method='uniform')
    lbp_hist,_ = np.histogram(lbp.ravel(),bins=np.arange(0, 11), density=True)
    
    return np.concatenate([hog_feat, lbp_hist])'''
def extract_features_from_folder(folder_path):
    features = []
    labels = []

    for label in os.listdir(folder_path):
        class_path = os.path.join(folder_path, label)
        for filename in os.listdir(class_path):
            img_path = os.path.join(class_path, filename)
            img = cv2.imread(img_path)
            if img is None:
                continue

            img = cv2.resize(img, (128, 128))
            gray = color.rgb2gray(img)

            hog_feat = hog(gray, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=False)
            features.append(hog_feat)
            labels.append(label)

    X = np.array(features)
    y = np.array(labels)

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    return X, y_encoded, le