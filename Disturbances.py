from StateSpaceModel import StateSpaceModel
import numpy as np
from ModelInput import ModelInput
class Disturbances:
    def __init__(self,
        covarianceDist: float,
        covarianceNoise: float,
        daug: [],
        inputSignal: ModelInput,
    ):
        self.Vd = covarianceDist*np.eye(4)
        self.Vn = covarianceNoise
        self.D = np.array(daug) #np.array(np.array(daug))
        self.model = inputSignal
        self.t = inputSignal.t



    def Builder(self):
        A, B, C, U = self.model.Builder()
        uDIST = np.sqrt(self.Vd) @ np.random.randn(4, len(U))  # random disturbance
        uNOISE = np.sqrt(self.Vn) * np.random.randn(len(U))  # random noise
        U = np.concatenate((U.reshape((1, len(U))), uDIST, uNOISE.reshape((1, len(uNOISE))))).T
        B = np.concatenate((B, np.eye(4), np.zeros_like(B)), axis=1)  # [u I*wd I*wn]
        C = np.array([1 , 0, 0 ,0])
        return A, B, C, self.D, U



