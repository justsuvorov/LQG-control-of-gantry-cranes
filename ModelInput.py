from StateSpaceModel import StateSpaceModel
import numpy as np

class ModelInput:
    def __init__(self,
                 index,
                 dt,
                 model : StateSpaceModel,
                 t = None,
                 u=None,
                 Force = None,
                 signal = None,
                 ):
        self.index = index
        self.dt = dt
        self.time = t
        self.Force = Force
        self.u = u
        self.t = []
        self.output = []
        self.C = []
        self.A,self.B = model.modelbuilder()


    def Builder(self):
        if self.index == 1:
            self.time = len(self.u) * self.dt
            self.t = np.arange(0, self.time, self.dt)
            self.output = np.array(self.u).T
            self.C = np.eye(4)
            return self.A, self.B, self.C, self.output

    def _force(self):
        self.t = np.arange(0, self.time, self.dt)
        self.u = np.zeros_like(self.t)

        # u[100] = 20 / dt  # positive impulse
        # u[1500] = -20 / dt  # negative impulse
        self.u = self.Force(self.t)