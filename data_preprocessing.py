import os
import cv2
import numpy as np
import pandas as pd
from pathlib import Path

DATA_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"

def preprocess_images():
    """Resize images and save them to the processed folder."""
    if not os.path.exists(PROCESSED_PATH):
        os.makedirs(PROCESSED_PATH)

    for img_file in os.listdir(DATA_PATH):
        img_path = os.path.join(DATA_PATH, img_file)
        img = cv2.imread(img_path)
        if img is not None:
            resized_img = cv2.resize(img, (224, 224))  # Resize to 224x224
            cv2.imwrite(os.path.join(PROCESSED_PATH, img_file), resized_img)

if __name__ == "__main__":
    preprocess_images()
