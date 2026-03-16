from mnist.mse import MSE

class SequentialNetwork:
    def __init__(self, loss=None):
        print("Initialize network...")
        self.layers = []
        if loss is None:
            self.loss = MSE()
