import numpy as np
from neural.utils import sigmoid

def sigmoid_prime_double(x):
    return sigmoid_double(x) * (1 - sigmoid_double(x))

def sigmoid_prime(z):
    return np.vectorize(sigmoid_prime_double)(z)

# Base class for the actual layer types (see below)
class Layer:
    def __init__(self):
        self.params = []

        self.previous = None
        self.next = None

        self.input_data = None
        self.output_data = None

        self.input_delta = None
        self.output_delta = None

    # Connect the layer to the next one
    def connect(self, layer):
        self.previous = layer
        layer.next = self

    def forward(self):
        raise NotImplementedError

    # Input data is reserved for the first layer;
    # all others get their input from the previous layer
    def get_forward_input(self):
        if self.previous is not None:
            return self.previous.output_data
        else:
            return self.output_data

    def backward(self):
        raise NotImplementedError

    # Input delta is reserved for the last layer;
    # all other layers get their error terms from their successor
    def get_backward_input(self):
        if self.next is not None:
            return self.next.output_delta
        else:
            return self.input_delta

    def clear_deltas(self):
        pass

    # Update layer parameters according to current deltas, using the
    # specified learning_rate
    def update_params(self, learning_rate):
        pass

    # Print the properties of this layer
    def describe(self):
        raise NotImplementedError



# This layer uses the sigmoid function to activate neurons
class ActivationLayer(Layer):
    def __init__(self, input_dim):
        super(ActivationLayer, self).__init__()
        self.input_dim = input_dim
        self.output_dim = input_dim

    # The forward pass applies the sigmoid function to the data
    def forward(self):
        data = self.get_forward_input()
        self.output_data = sigmoid(data)

    # The backward pass is element-wise multiplication of
    # the error term with the sigmoid derivative evaluated at
    # the input of this layer: σ(x) · (1 – σ(x)) · Δ
    def backward(self):
        delta = self.get_backward_input()
        data = self.get_forward_input()
        self.output_delta = delta * sigmoid_prime(data)

    def describe(self):
        print("|-- " + self.__class__.__name__)
        print("  |-- dimensions: ({},{})".format(self.input_dim, self.output_dim))


class DenseLayer(Layer):
    def __init__(self, input_dim, output_dim):
        super(DenseLayer, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.weight = np.random.randn(output_dim, input_dim)
        self.bias = np.random.randn(output_dim, 1)
        self.params = [self.weight, self.bias]
        self.delta_w = np.zeros(self.weight.shape)
        self.delta_b = np.zeros(self.bias.shape)

    # The forward pass of the dense layer is the affine-linear
    # transformation on input data defined by weights and biases
    def forward(self):
        data = self.get_forward_input()
        self.output_data = np.dot(self.weight, data) + self.bias

    def backward(self):
        data = self.get_forward_input()
        delta = self.get_backward_input()
        self.delta_b += delta
        self.delta_w += np.dot(delta, data.transpose())
        self.output_delta = np.dot(self.weight.transpose(), delta)

    # Gradient descent
    def update_params(self, rate):
        self.weight -= rate * self.delta_w
        self.bias -= rate * self.delta_b

    def clear_deltas(self):
        self.delta_w = np.zeros(self.weight.shape)
        self.delta_b = np.zeros(self.bias.shape)

    def describe(self):
        print("|--" + self.__class__.__name__)
        print("  |-- dimensions: ({},{})".format(self.input_dim, self.output_dim))
