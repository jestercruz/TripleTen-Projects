import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, AvgPool2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np


def load_train(path):
    features_train = np.load(path + 'train_features.npy')
    target_train = np.load(path + 'train_target.npy')
    features_train = features_train.reshape(-1, 28, 28, 1) / 255.0
    return features_train, target_train

def create_model(input_shape):
    model = Sequential()
    model.add(
    Conv2D(6, (5, 5), padding='same', activation='tanh', input_shape=(28, 28, 1)))
    model.add(AvgPool2D(pool_size=(2, 2)))
    model.add(Conv2D(16, (5, 5), padding='valid', activation='tanh'))
    model.add(AvgPool2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(120, activation='tanh'))
    model.add(Dense(84, activation='tanh'))
    model.add(Dense(10, activation='softmax'))
   
    optimizer = Adam(lr=0.01)
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['acc'],
    )
    return model

def train_model(model, train_data, test_data, batch_size=32, epochs=10,
                steps_per_epoch=None, validation_steps=None):
    features_train, target_train = train_data
    features_test, target_test = test_data
    model.fit(features_train, target_train,
              validation_data=(features_test, target_test),
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2, shuffle=True)

    return model