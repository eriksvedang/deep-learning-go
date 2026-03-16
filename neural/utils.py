import numpy as np
import struct
import six.moves.cPickle as pickle
import gzip
from matplotlib import pyplot as plt

"""One hot encoding."""
def encode_label(j):
    e = np.zeros((10, 1))
    e[j] = 1
    return e

def shape_data(data):
    features = [np.reshape(x, (784, 1)) for x in data[0]] # Flatten image to a vector
    labels = [encode_label(y) for y in data[1]]
    return list(zip(features, labels))

def load_data():
    with gzip.open('./neural/mnist.pkl.gz', 'rb') as f:
        train_data, validation_data, test_data = pickle.load(f, encoding='bytes')
        f.close()
    return shape_data(train_data), shape_data(test_data)

def show(image_data):
    img = np.reshape(image_data, (28, 28))
    plt.imshow(img)
    plt.show()

def sigmoid_double(x):
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid(z):
    return np.vectorize(sigmoid_double)(z)

def predict(x, W, b):
    return sigmoid_double(np.dot(W, x) + b)
