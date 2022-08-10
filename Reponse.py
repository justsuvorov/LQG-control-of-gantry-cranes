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
        self.A, self.B, self.C, self.D, self.U = model.Builder()
        self.sys = []
        self.index = index
        self.t = model.t
        self.y = [[]]

        self._ = [[]]
        self.X0 = X0

    def run(self):
        self._buildSystem()
        if self.index == 0:
            self._timeDomainResponse()
        if self.index == 1:
            self._stepResponse()



    def _buildSystem(self):
        self.sys = control.matlab.ss(self.A, self.B, self.C, self.D)

    def _stepResponse(self):
        self.y, self.t, self._ = control.matlab.step_response( self.sys, self.tm, self.X0)
        return self.y, self.t

    def _timeDomainResponse(self):

        self.y, self.t, self._ = control.matlab.lsim( self.sys, self.U, self.t)

        return self.y, self.t, self._
