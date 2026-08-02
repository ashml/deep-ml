import numpy as np

def calculate_brightness(img):
    if not img:
        return -1
	if any(len(row) != len(img[0]) for row in img):
        return -1
    img = np.array(img)
    if img.max() > 255 or img.min() < 0:
        return -1
    return img.mean()
