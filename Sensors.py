from StateSpaceModel import StateSpaceModel
import numpy as np
from ModelInput import ModelInput
from Disturbances import Disturbances
class Sensors():
    def __init__(self,
                 C : [],
                 model: Disturbances,
                 ):
        self.A, self.B, self.C, self.D, self.U = model.Builder()
        self.Csensors = np.array(C)
        self.t = model.t

    def Builder(self):
        self.C = self.Csensors
        return self.A, self.B, self.C, self.D, self.U