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
    with gzip.open('./mnist/mnist.pkl.gz', 'rb') as f:
        train_data, validation_data, test_data = pickle.load(f, encoding='bytes')
        f.close()
    return shape_data(train_data), shape_data(test_data)

def average_digit(data, digit):
    filtered_data = [x[0] for x in data if np.argmax(x[1]) == digit]
    filtered_array = np.asarray(filtered_data)
    return np.average(filtered_array, axis=0)

def show(image_data):
    img = np.reshape(image_data, (28, 28))
    plt.imshow(img)
    plt.show()

train, test = load_data()
avg_height = average_digit(train, digit=8)
#show(avg_height)

W = np.transpose(avg_height)
x_3 = train[2][0] # a 4
x_18 = train[17][0] # an 8
#show(x_18)
#print(np.dot(W, x_3))
#print(np.dot(W, x_18)) # This one is longer, since it matches the avg_height for the number 8

def sigmoid_double(x):
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid(z):
    return np.vectorize(sigmoid_double)(z)

def predict(x, W, b):
    return sigmoid_double(np.dot(W, x) + b)

b = -45
print(predict(x_3, W, b))
print(predict(x_18, W, b))
