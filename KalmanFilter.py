import control
import control.matlab
from Sensors import Sensors
import numpy as np
from StateSpaceModel import StateSpaceModel

class KalmanFilter:
    """
        Build Kalman Filter for a state-space representation of a gantry crane linear system.

        x' = Ax + Bu
        y = Cx + Du

        Parameters
        ----------
        t : time interval for a time domain response
        model : StateSpaceModel with matrices A, B, C, D
        Covariance of noise and disturbances


        Returns
        -------
        Modelbuilder : Matrix A, B, C, D for a time-domain analysis
        Kf : Kalman filter koefficients

        See Also https://en.wikipedia.org/wiki/Kalman_filter
        -------
        """
    def __init__(self,
                 model: Sensors,
                 ):
        self.model = model
        self.t = []

    def Builder(self):
        A, B, C, D, U = self.model.Builder()
        Vn = self.model.noise
        Vd = self.model.Vd
        Cc = np.array([1,0, 0, 0])
        Kf = control.lqe(A, np.eye(4), Cc, Vd, Vn)[0].T
        self.t = self.model.t
        print('Kalman Filter Coefficients: ', Kf)
        y, t, _ = control.matlab.lsim(control.matlab.ss(A, B, C, D), U, self.t)
        A = A - np.outer(Kf, C)
        C = np.eye(4)
        B = np.concatenate((B[:,:1], np.atleast_2d(Kf.T)), axis=1)
        D = np.zeros_like(B)
        U = np.column_stack((U[:,0].T, y))

        return A, B, C, D, U