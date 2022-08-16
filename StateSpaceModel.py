import numpy as np
import matplotlib.pyplot as plt
import control
import control.matlab
import slycot
from matplotlib import rcParams
from scipy import integrate
from scipy.linalg import schur

class StateSpaceModel:

    """Build a state-space representation of a gantry crane linear system.

    x' = Ax + Bu
    x : position, velocity of the trolley, angle and angle velocity of the load

    Parameters
    ----------
    m : mass of the load
    M : mass of the trolley
    L : length of the rope

    Returns
    -------
    Modelbuilder :

    Matrices A and B

    See Also https://en.wikipedia.org/wiki/State-space_representation
    --------

    """
    def __init__(self,
        mass: int,
        trolleyMass: int,
        length: float,
        g: float,
    ):
        self._m = mass
        self._tM = trolleyMass
        self._L = length
        self._g = g

    def modelbuilder(self):
        A = np.array([[0, 1, 0, 0], \
                      [0, 0, -((self._g * self._m) / self._tM), 0], \
                      [0, 0, 0, 1], \
                      [0, 0, -((self._g * (-self._m - self._tM)) / (self._L * self._tM)), 0]])

        B = np.array([0, 1 / self._tM, 0, - 1 / (self._L * self._tM)]).reshape((4, 1))
        return A, B