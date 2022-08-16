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
        self.t = []
        self.noise = model.Vn
        self.Vd = model.Vd

    def Builder(self):
        Cc = self.Csensors
        A, B, C, D, U = self.model.Builder()
        self.t = self.model.t
        return A, B, Cc, D, U