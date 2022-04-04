# Import Modules
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

class AIModel:

    # Define Constants
    SAVED_MODEL_PATH = 'saved\models\my_model'
    IMG_SIZE = 180

    def __init__(self):
  
        # Define Sequential Model
        model = Sequential()

        # 
        model.add(Conv2D(64, (3, 3), input_shape = (180, 180, 1)))
        model.add(Activation('relu')) # get rid of waste data
        model.add(MaxPooling2D(pool_size=(2, 2))) # pool windows together

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu')) # get rid of waste data
        model.add(MaxPooling2D(pool_size=(2, 2))) # pool windows together

        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
        model.add(Dense(64)) # links all nodes to all other nodes

        model.add(Dense(1)) # link to end layer
        model.add(Activation('sigmoid')) # output of classification is continuous

        model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

        # Create a basic model instance
        model.load_weights(AIModel.SAVED_MODEL_PATH)

        # Initialise Attr
        self.model = model

    def predictInstance(self, filepath):

        # Process the image
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE) # reads and convs to grayscale
        resized_img = cv2.resize(img, (AIModel.IMG_SIZE, AIModel.IMG_SIZE)) # resizes to smaller size
        test_example = np.array(resized_img).reshape(-1, AIModel.IMG_SIZE, AIModel.IMG_SIZE, 1)

        # Predict the class
        result = self.model.predict(test_example)[0][0]
        return not bool(result)


def main():
    m = AIModel()
    results = []
    for i in range(1, 8):
        results.append(m.predictInstance("static/trains/"+str(i)+".jpg"))
    print(results)

if __name__ == "__main__":
    main()
