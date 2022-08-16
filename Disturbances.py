from StateSpaceModel import StateSpaceModel
import numpy as np
from ModelInput import ModelInput
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
        self.Vn = covarianceNoise
        self.D = np.array(daug) #np.array(np.array(daug))
        self.model = inputSignal
        self.t = []

    def builder(self):
        vD = self._covarianceDist * np.eye(4)
        A, B, C, U = self.model.builder()
        self.t = self.model.t
        uDIST = np.sqrt(vD) @ np.random.randn(4, len(U))  # random disturbance
        uNOISE = np.sqrt(self.Vn) * np.random.randn(len(U))  # random noise
        U = np.concatenate((U.reshape((1, len(U))), uDIST, uNOISE.reshape((1, len(uNOISE))))).T
        B = np.concatenate((B, np.eye(4), np.zeros_like(B)), axis=1)  # [u I*wd I*wn]
        C = np.array([1, 0, 0, 0])
        return A, B, C, self.D, U