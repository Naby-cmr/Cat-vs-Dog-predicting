import cv2
import numpy as np
from keras.models import load_model
model = load_model('models/model.h5')


def predict(img_decoded):
    model = load_model('models/model.h5')
    resized_image = cv2.resize(img_decoded, (200,200))
    resized_image = resized_image / 255.0
    image_array = np.array(resized_image).reshape(1, 200, 200, 3)
    predictions = model.predict(image_array)
    return predictions 

