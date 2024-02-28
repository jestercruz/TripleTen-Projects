# from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np


# In[2]:


def load_train(path):
    features_train = np.load(path + 'train_features.npy')
    target_train = np.load(path + 'train_target.npy')
    features_train = features_train.reshape(features_train.shape[0], 28 * 28) / 255.
    return (features_train, target_train)

def load_test(path):
    features_train = np.load(path + 'test_features.npy')
    target_train = np.load(path + 'test_target.npy')
    features_train = features_train.reshape(features_train.shape[0], 28 * 28) / 255.
    return (features_train, target_train)


def create_model(input_shape):
    model = Sequential()
    model.add(Dense(512, input_shape=input_shape, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(optimizer = 'sgd', loss = 'sparse_categorical_crossentropy', metrics = ['acc'])
    return model


# In[4]:


def train_model(
    model,
    train_data,
    test_data,
    batch_size = 32,
    epochs = 5,
    steps_per_epoch = None,
    validation_steps = None,
):

    features_train, target_train = train_data
    features_test, target_test = test_data
    model.fit(
        features_train,
        target_train,
        validation_data = (features_test, target_test),
        batch_size = batch_size,
        epochs = epochs,
        steps_per_epoch = steps_per_epoch,
        validation_steps = validation_steps,
        verbose = 2,
        shuffle = True,
    )

    return model


# In[5]:


# fashion_data = fashion_mnist

# train_data = load_train(fashion_data)
# test_data = load_test(fashion_data)


# In[6]:


if __name__ == "__main__":
    train_data = load_train("/datasets/fashion_mnist/")
    test_data = load_test("/datasets/fashion_mnist/")
    model = create_model(train_data[0].shape[1:])
    model = train_model(model, train_data, test_data)
    loss, acc = model.evaluate(test_data[0], test_data[1], verbose=2)
    print("Model accuracy: {:5.2f}%".format(100 * acc))