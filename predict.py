from keras.models import load_model
import cv2
import numpy as np

img_name = "images/user_image_hw.jpg"

model = load_model('models/cnn_mnist.h5')


img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img, (28, 28))
img = img.reshape(1, 28, 28)
img = img / 255

prediction = model.predict(img)
digit = np.argmax(prediction)

print(digit)
