# utils/io_utils.py
import json
from PIL import Image
import numpy as np

def read_scene_from_json(file_path):
    with open(file_path, 'r') as file:
        scene_data = json.load(file)
    return scene_data

def save_image(image_array, file_path):
    image = Image.fromarray(image_array.astype(np.uint8))
    image.save(file_path)
