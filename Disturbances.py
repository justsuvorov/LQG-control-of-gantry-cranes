from StateSpaceModel import StateSpaceModel
import numpy as np
from ModelInput import ModelInput
class Disturbances:
    def __init__(self,
               covarianceDist,
               covarianceNoise,
               Daug: [],
               inputSignal: ModelInput,
                              ):
        self.Vd = covarianceDist*np.eye(4)
        self.Vn = covarianceNoise
        self.D = np.array(Daug)
        self.A, self.B, self.C, self.U = inputSignal.Builder()
        self.t = inputSignal.t
        self.uDIST = [[]]
        self.uNOISE = [[]]
        self.t = inputSignal.t

    def Builder(self):
        self.uDIST = np.sqrt(self.Vd) @ np.random.randn(4, len(self.U))  # random disturbance
        self.uNOISE = np.sqrt(self.Vn) * np.random.randn(len(self.U))  # random noise
        self.U = np.concatenate((self.U.reshape((1, len(self.U))), self.uDIST, self.uNOISE.reshape((1, len(self.uNOISE))))).T
        self.B = np.concatenate((self.B, np.eye(4), np.zeros_like(self.B)), axis=1)  # [u I*wd I*wn]
        self.C = np.array([1 , 0, 0 ,0])
        return self.A, self.B, self.C, self.D, self.U



