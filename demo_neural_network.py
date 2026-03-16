from neural.network import SequentialNetwork
from neural.layers import DenseLayer, ActivationLayer
from neural.utils import load_data

training_data, test_data = load_data()

net = SequentialNetwork()

net.add(DenseLayer(784, 392))
net.add(ActivationLayer(392))
net.add(DenseLayer(392, 196))
net.add(ActivationLayer(196))
net.add(DenseLayer(196, 10))
net.add(ActivationLayer(10))
