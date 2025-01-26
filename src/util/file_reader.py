import csv
import io
import urllib.request
import cv2
import base64
import numpy as np
from PIL import Image
from numpy import ndarray


def pil_to_rgb(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)


def base64_to_img(base64_string) -> ndarray:
    imgdata = base64.b64decode(base64_string)
    return pil_to_rgb(Image.open(io.BytesIO(imgdata)))


def read_csv(filename: str):
    with open(filename, "r") as file:
        csv_dict = csv.DictReader(file)
        return [entry for entry in csv_dict]


def serialize_items(items: list, object):
    return [object(entry).__dict__ for entry in items]


def fetch_image_from_url(url: str) -> ndarray:
    req = urllib.request.urlopen(url)
    image = np.asarray(bytearray(req.read()), dtype=np.uint8)
    return cv2.imdecode(image, -1)
