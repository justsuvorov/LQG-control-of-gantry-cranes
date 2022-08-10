import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

import control
import control.matlab
import slycot
from scipy import integrate
from scipy.linalg import schur
class StateSpaceModel:
    def __init__(self,
                 mass,
                 trolleyMass,
                 length
                 ):
        self.m = mass
        self.M = trolleyMass
        self.L = length
        self.g = -10
        self.A = [[]]
        self.B = [[]]

    def modelbuilder(self):
        self.A = np.array([[0, 1, 0, 0], \
                      [0, 0, -((self.g * self.m) / self.M), 0], \
                      [0, 0, 0, 1], \
                      [0, 0, -((self.g * (-self.m - self.M)) / (self.L * self.M)), 0]])

        self.B = np.array([0, 1 / self.M, 0, - 1 / (self.L * self.M)]).reshape((4, 1))
        return self.A, self.B

