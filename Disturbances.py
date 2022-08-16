from StateSpaceModel import StateSpaceModel
import numpy as np
from ModelInput import ModelInput
from response_result import ResponseResult

class Disturbances:
    """
        Build vectors of Gaussian disturbances and noise for vector X as new matrices D and U

        x' = Ax + Bu
        y = Cx + Du

        Parameters
        ----------
        Inputs:

        covariance of disturbances: covariance of disturbances for a diagonal matrix of covariance
        covariance of noise
        daug: matrix passes disturbances and noise through for vector x and y like [F, x, v, fi, omega, y]
        inputSignal: Input for the model and simulation


        Returns
        -------
        Modelbuilder : Matrices A, B, C, D, matrix of loads U
        vector of time for a time-domain analysis

        See Also https://en.wikipedia.org/wiki/State-space_representation
        -------

        """
    def __init__(self,
        covarianceDist: float,
        covarianceNoise: float,
        daug: [],
        inputSignal: ModelInput,
    ):
        self._covarianceDist = covarianceDist
        self._Vn = covarianceNoise
        self._D = np.array(daug) #np.array(np.array(daug))
        self.model = inputSignal

    def builder(self):
        vD = self._covarianceDist * np.eye(4)
        result = self.model.builder()
        uDIST = np.sqrt(vD) @ np.random.randn(4, len(result.U))  # random disturbance
        uNOISE = np.sqrt(self._Vn) * np.random.randn(len(result.U))  # random noise
        U = np.concatenate((result.U.reshape((1, len(result.U))), uDIST, uNOISE.reshape((1, len(uNOISE))))).T
        B = np.concatenate((result.B, np.eye(4), np.zeros_like(result.B)), axis=1)  # [u I*wd I*wn]
        C = np.array([1, 0, 0, 0])
        return ResponseResult(A = result.A,
                              B = B,
                              C = C,
                              D = self._D,
                              U = U,
                              t = result.t,
                              Vd = vD,
                              Vn = self._Vn,
        )