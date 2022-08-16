import control
import control.matlab
from Sensors import Sensors
import numpy as np

class KalmanFilter:
    def __init__(self,
                 model: Sensors
                 ):
        self.model = model
        self.t = []

    def Builder(self):
        A, B, C, D, U = self.model.Builder()
        Vn = self.model.noise
        Vd = self.model.Vd
        Cc = np.array([1,0, 0, 0])
        Kf, P, E = control.lqe(A, np.eye(4), Cc, Vd, Vn)
        Kf = Kf.T
        self.t = self.model.t
        print('Kalman Filter Coefficients: ', Kf)
        A = A - np.outer(Kf, C)
        return A, B, C, D, U