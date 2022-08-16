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
    def __init__(self,
        index,
        modelfilter: KalmanFilter = None,
        modelsensors: Sensors = None,
        statespacemodel: ModelInput = None,
        modeldisturbances:  Disturbances = None,
        X0: [] = None,
    ):
        self.sys = []
        self.index = index
        self.y = [[]]
        self._ = [[]]
        self.x0 = X0
        if modelfilter != None: self.model = modelfilter
        if modelsensors != None: self.model = modelsensors
        if modelsensors != None: self.model = modelsensors
        if modeldisturbances != None: self.model = modeldisturbances
        if statespacemodel != None: self.model = statespacemodel

    def run(self):
        if self.model == None : raise Exception('No model')
        A, B, C, D, U = self.model.Builder()
        if self.index == 0:
            return self._timeDomainResponse(
                self._buildSys(A, B, C, D),
                U,
                self.model.t,
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
            t = t,
            y = y,
            _ = y
        )

    def _timeDomainResponse(self, sys, u, t):
        y, t, _ = control.matlab.lsim( sys, u, t)
        return ResponseResult(
            t = t,
            y = y,
            _ = _,
        )