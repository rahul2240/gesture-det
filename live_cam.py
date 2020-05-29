import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import imutils

np.set_printoptions(suppress=True)


model = tensorflow.keras.models.load_model('keras_model.h5')

classes = ["pick", "swap", "flying plane", "move", "move up", "cancel", "rotate"]
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    ret, frame = cap.read()

    frame = imutils.resize(frame, width = 400)
    image = frame.copy()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)

    #print(image.shape)
    size = (224, 224)

    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)

    cv2.imshow('prediction ', frame)  
    print(classes[np.argmax(prediction)])    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

