from Disturbances import Disturbances
import control
import control.matlab
from Sensors import Sensors
from response_result import ResponseResult
from KalmanFilter import KalmanFilter
import numpy as np

class LQR:
    """
        Build LQR control for a state-space representation of a gantry crane linear system.

        x' = Ax + Bu
        y = Cx + Du

        Parameters
        ----------
        t : time interval for a time domain response
        model : StateSpaceModel with matrices A, B, C, D
        Q and R : weights of the parameters for optimal control


        Returns
        -------
        Modelbuilder : Matrix A, B, C, D for a time-domain analysis
        LQR : LQR gains

        See Also https://en.wikipedia.org/wiki/Linear%E2%80%93quadratic_regulator
        -------
        """
    def __init__(self,
                  q,
                  r,
                 modelsensors: Sensors = None,
                 modelfilter: KalmanFilter = None,
                ):
        self.q = q
        self.r = r
        if modelsensors != None: self.model = modelsensors
        if modelfilter != None: self.model = modelfilter

    def builder(self):
        result = self.model.builder()
        Q = np.array([[self.q, 0, 0, 0], \
              [0, self.q,0, 0], \
              [0, 0, self.q, 0], \
              [0, 0, 0, self.q]])
        R = self.r
        kLQR = control.lqr(result.A, result.B[:, :1], Q, R)[0]
        print('LQR Gains: ', kLQR)
        A = result.A - np.outer(result.B[:, :1], kLQR.T)

        return ResponseResult(A = A,
                              B = result.B,
                              C = result.C,
                              D = result.D,
                              U = result.U,
                              t = result.t,)



