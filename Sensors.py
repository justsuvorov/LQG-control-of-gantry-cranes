import numpy as np
from ModelInput import ModelInput
from Disturbances import Disturbances
class Sensors():
    def __init__(self,
        C : [],
        model: Disturbances,
    ):

        self.Csensors = np.array(C)
        self.model = model
        self.t = model.t
        self.noise = model.Vn
        print(model.t)

    def Builder(self):
        Cc = self.Csensors
        A, B, C, D, U = self.model.Builder()
        return A, B, Cc, D, U