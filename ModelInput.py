from StateSpaceModel import StateSpaceModel
import numpy as np
from response_result import ResponseResult

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
        signal: list = None,
    ):
        self.loadIndex = loadIndex
        self.dt = dt
        self.model = model
        self.time = time
        self.u = u
        self.force = force
        self.signal = signal

    def builder(self):
        result = self.model.modelbuilder()
        if self.loadIndex == 1:
            self.time = len(self.u) * self.dt
            t = np.arange(0, self.time, self.dt)

            output = np.array(self.u).T
            C = np.eye(4)
            return ResponseResult(A = result.A,
                                  B = result.B,
                                  C = C,
                                  U = output,
                                  t = t)
        elif self.loadIndex == 2:

            u = self.signal
            t = np.arange(0, self.time, self.dt)
            u1 = np.full_like(t, self.u[0])  # coordinate
            u2 = np.full_like(t, -self.u[1])  # velocity
            u3 = np.full_like(t, self.u[2])  # angle
            u4 = np.full_like(t, self.u[3])  # angle velocity
            u5 = np.full_like(t, self.u[4])
            u6 = np.full_like(t, self.u[0])  # y
            output = np.concatenate((u1.reshape((1, len(u2))), u2.reshape((1, len(u2))), u3.reshape((1, len(u2))),
                       u4.reshape((1, len(u2))),u5.reshape((1, len(u2))),u6.reshape((1, len(u2)))))
            C = np.eye(4)
            return ResponseResult(A=result.A,
                                  B=result.B,
                                  C= C,
                                  U=output,
                                  t=t)
        else:
            raise Exception('This case not implemented yet.')

    def _force(self):
        self.t = np.arange(0, self.time, self.dt)
        self.u = np.zeros_like(self.t)
        # u[100] = 20 / dt  # positive impulse
        # u[1500] = -20 / dt  # negative impulse
        self.u = self.Force(self.t)

    def _signal(self):
        u = self.self.signal
        u1 = np.full_like(t, 0)  # coordinate
        u2 = np.full_like(t, -0.3)  # velocity
        u3 = np.zeros_like(t)  # angle
        u4 = np.zeros_like(t)  # angle velocity
        u5 = np.zeros_like(t)
        u6 = np.zeros_like(t)  # y