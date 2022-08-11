from StateSpaceModel import StateSpaceModel
import numpy as np

class ModelInput:
    def __init__(self,
        loadIndex: float,
        dt: float,
        model: StateSpaceModel,
        t: float = None,
        u = None,
        Force = None,
        signal = None,
    ):
        self.loadIndex = loadIndex
        self.dt = dt
        self.time = t
        self.Force = Force
        self.u = u
        self.t = []
        self.output = []
        self.model = model


    def Builder(self):
        if self.loadIndex == 1:
            self.time = len(self.u) * self.dt
            self.t = np.arange(0, self.time, self.dt)
            output = np.array(self.u).T
            A, B = self.model.modelbuilder()
            C = np.eye(4)

            return A, B, C, output

    def _force(self):
        self.t = np.arange(0, self.time, self.dt)
        self.u = np.zeros_like(self.t)
        print(self.t)

        # u[100] = 20 / dt  # positive impulse
        # u[1500] = -20 / dt  # negative impulse
        self.u = self.Force(self.t)