import numpy as np
import struct
import six.moves.cPickle as pickle
import gzip
from matplotlib import pyplot as plt
import neural as neural

def average_digit(data, digit):
    filtered_data = [x[0] for x in data if np.argmax(x[1]) == digit]
    filtered_array = np.asarray(filtered_data)
    return np.average(filtered_array, axis=0)

train, test = neural.load_data()
avg_height = average_digit(train, digit=8)
#show(avg_height)

W = np.transpose(avg_height)
x_3 = train[2][0] # a 4
x_18 = train[17][0] # an 8
#show(x_18)
#print(np.dot(W, x_3))
#print(np.dot(W, x_18)) # This one is longer, since it matches the avg_height for the number 8

b = -45
#print(neural.predict(x_3, W, b))
#print(neural.predict(x_18, W, b))

def evaluate(data, digit, threshold, W, b):
    total_samples = 1.0 * len(data)
    correct_predictions = 0
    for x in data:
        if neural.predict(x[0], W, b) > threshold and np.argmax(x[1]) == digit:
            correct_predictions += 1
        elif neural.predict(x[0], W, b) <= threshold and np.argmax(x[1]) != digit:
            correct_predictions += 1
    return correct_predictions / total_samples

for digit in range(0, 10):
    print("%d: %f" % (digit, evaluate(data=test, digit=digit, threshold=0.5, W=W, b=b)))
