from neural.mse import MSE

class SequentialNetwork:
    def __init__(self, loss=None):
        print("Initialize network...")
        self.layers = []
        if loss is None:
            self.loss = MSE()

    # Add layers sequentially
    def add(self, layer):
        self.layers.append(layer)
        layer.describe()
        if len(self.layers) > 1:
            self.layers[-1].connect(self.layers[-2])
