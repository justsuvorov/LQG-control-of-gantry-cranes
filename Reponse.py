from StateSpaceModel import StateSpaceModel
import numpy as np
from ModelInput import ModelInput
from Disturbances import Disturbances
import control
import control.matlab
from Sensors import Sensors

class Response:
    def __init__(self,
        index,
        model: Sensors,
        X0: [] = None
    ):
        self.sys = []
        self.index = index
        self.t = model.t
        self.y = [[]]
        self._ = [[]]
        self.x0 = X0

    def run(self):
        A, B, C, D, U = model.Builder()
        if self.index == 0:
            return self._timeDomainResponse(
                self._buildSys(A, B, C, D),
                U,
                self.t,
            )
        if self.index == 1:
            return self._stepResponse(
                self._buildSys(A, B, C, D),
                tm,
                self.x0,
            )



    def _buildSys(self, A, B, C, D):
        return control.matlab.ss(A, B, C, D)

    def _stepResponse(self, sys, tm, x0):
        y, t, _ = control.matlab.step_response( sys, tm, x0)
        return ResponseResult(
            t = t,
            y = y,
            _ = _,
        )

    def _timeDomainResponse(self, sys, u, t):
        y, t, _ = control.matlab.lsim( sys, u, t)
        return ResponseResult(
            t = t,
            y = y,
            _ = _,
        )
