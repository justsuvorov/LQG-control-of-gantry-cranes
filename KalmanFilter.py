import control
import control.matlab
from Sensors import Sensors
import numpy as np
from StateSpaceModel import StateSpaceModel
from response_result import ResponseResult

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

    def builder(self):
        result = self.model.builder()
        matrixC = np.array([1,0, 0, 0])
        Kf = control.lqe(result.A, np.eye(4), matrixC, result.Vd, result.Vn)[0].T
        t = result.t
        print('Kalman Filter Coefficients: ', Kf)
        y, t, _ = control.matlab.lsim(control.matlab.ss(result.A, result.B, result.C, result.D), result.U, result.t)
        A = result.A - np.outer(Kf, result.C)
        C = np.eye(4)
        B = np.concatenate((result.B[:,:1], np.atleast_2d(Kf.T)), axis=1)
        D = np.zeros_like(B)
        U = np.column_stack((result.U[:,0].T, y))

        return ResponseResult(A = A,
                              B = B,
                              C = C,
                              D = D,
                              U = U,
                              t = result.t,

        )