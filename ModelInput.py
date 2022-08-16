from StateSpaceModel import StateSpaceModel
import numpy as np

class ModelInput:

    """
    Build an input U and matrices C, D for a state-space representation of a gantry crane linear system.

    x' = Ax + Bu
    y = Cx + Du

    Parameters
    ----------
    dt : time discretization for a simulation
    t : time interval for a time domain response
    model : StateSpaceModel with matrices A and B

    Inputs:
    u : vector of loads
    or
    Force : function of the load
    or
    Signal: X setpoint as Heaviside function like [0, 0.3, 0, 0] (position, velocity, angle and angle veolicty)

    Returns
    -------
    Modelbuilder : Matrix of loads U and matrix C
    vector of time for a time-domain analysis

    See Also https://en.wikipedia.org/wiki/State-space_representation
    -------

    """
    def __init__(self,
        loadIndex: float,
        dt: float,
        model: StateSpaceModel,
        time: float = None,
        u: list = None,
        force = None,
        signal = None,
    ):
        self.loadIndex = loadIndex
        self.dt = dt
        self.model = model
        self.time = time
        self.u = u
        self.force = force
        self.t = []
        self.output = []

    def builder(self):
        if self.loadIndex == 1:
            self.time = len(self.u) * self.dt
            self.t = np.arange(0, self.time, self.dt)
            output = np.array(self.u).T
            A, B = self.model.modelbuilder()
            C = np.eye(4)
            return A, B, C, output
        else:
            raise Exception('This case not implemented yet.')

    def _force(self):
        self.t = np.arange(0, self.time, self.dt)
        self.u = np.zeros_like(self.t)
        # u[100] = 20 / dt  # positive impulse
        # u[1500] = -20 / dt  # negative impulse
        self.u = self.Force(self.t)