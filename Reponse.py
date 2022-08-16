from StateSpaceModel import StateSpaceModel
import numpy as np
from ModelInput import ModelInput
from Disturbances import Disturbances
import control
import control.matlab
from Sensors import Sensors
from response_result import ResponseResult
from KalmanFilter import KalmanFilter
class Response:
    """
        Build a time-domain response for a state-space representation of a gantry crane linear system.

        x' = Ax + Bu
        y = Cx + Du

        Parameters
        ----------
        Inputs

        model : State Space Model with matrices A, B, C, D
        U: matrix of inputs
        index: 0 for time-domain response and 1 for a step response
        initial state X0 as vector of coordinates [x, v, fi, omega]

        Returns
        -------
        Modelbuilder : array of the state response [x, v, fi, omega] and vector of time t
        Kf : Kalman filter coefficients

        See Also https://python-control.readthedocs.io/en/latest/generated/control.matlab.lsim.html?highlight=lsim
                https://python-control.readthedocs.io/en/latest/generated/control.matlab.step.html
        -------
        """
    def __init__(self,
        index,
        modelfilter: KalmanFilter = None,
        modelsensors: Sensors = None,
        modeldisturbances:  Disturbances = None,
        X0: [] = None,
    ):
        self.sys = []
        self.index = index
        self.x0 = X0
        if modelfilter != None: self.model = modelfilter
        if modelsensors != None: self.model = modelsensors
        if modeldisturbances != None: self.model = modeldisturbances

    def run(self):
        if self.model == None : raise Exception('No model')
        result = self.model.builder()
        A = result.A
        B = result.B
        C = result.C
        D = result.D
        U = result.U
        if self.index == 0:
            return self._timeDomainResponse(
                self._buildSys(A, B, C, D),
                U,
                result.t,
            )
        if self.index == 1:
            return self._stepResponse(
                self._buildSys(A, B, C, D),
                self.x0,
            )

    def _buildSys(self, A, B, C, D):
        return control.matlab.ss(A, B, C, D)

    def _stepResponse(self, sys, tm, x0 = 0):
        y, t = control.step_response(sys, tm, X0 = 0)
        return ResponseResult(
            A = 0,
            B = 0,
            t = t,
            y = y,
            _ = y
        )

    def _timeDomainResponse(self, sys, u, t):
        y, t, _ = control.matlab.lsim( sys, u, t)
        return ResponseResult(
            A = 0,
            B = 0,
            t = t,
            y = y,
            _ = _,
        )