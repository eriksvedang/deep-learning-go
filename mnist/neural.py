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
    return zip(features, labels)

def load_data():
    with gzip.open('./mnist/mnist.pkl.gz', 'rb') as f:
        train_data, validation_data, test_data = pickle.load(f, encoding='bytes')
        f.close()
    return shape_data(train_data), shape_data(test_data)

def average_digit(data, digit):
    filtered_data = [x[0] for x in data if np.argmax(x[1]) == digit]
    filtered_array = np.asarray(filtered_data)
    return np.average(filtered_array, axis=0)

train, test = load_data()
avg_height = average_digit(train, digit=4)
img = np.reshape(avg_height, (28, 28))
plt.imshow(img)
plt.show()
