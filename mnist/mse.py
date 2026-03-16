import random
import numpy as np

# Mean Squared Error
class MSE:
    def __init__(self):
        pass

    @staticmethod
    def loss_function(predictions, labels):
        diff = predictions - labels
        return 0.5 * sum(diff * diff)[0]

    @staticmethod
    def loss_derivate(predictions, labels):
        return predictions - labels
