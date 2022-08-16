from StateSpaceModel import StateSpaceModel
from ModelInput import ModelInput
import numpy as np
from Disturbances import Disturbances
from Sensors import Sensors
from Reponse import Response
from KalmanFilter import KalmanFilter
from Plot import Plot

def force(t):
    """
    The function of force acting on the trolley
    :param t:
    :return: F, N
    """
    F = 59.5394 * np.exp(-247.492 * t) - 365.263* np.exp(-50. * t) + \
        47.2495 * np.exp(-7.39438 * t) + (99.4454 -
    201.182 *  1j) * np.exp((-5.61451 - 4.92613 * 1j) * t) + (99.4454 +
    201.182 * 1j ) * np.exp((-5.61451 + 4.92613 * 1j) * t) + 59.5829 * np.exp(-1.33333 * t)
    return F.real

#Входные параметры системы
m = 15 #load weight
M = 80 #trolley weight
L = 1.15 #length of the rope
g = -10  #g
Vd = 0.00001  # distrubance covariance
Vn = 0.01  # noise covariance
D= [0, 0, 1, 1, 1, 1]  # D matrix passes noise and disturbances through [F,x,v,fi,omega,y]
dt = 0.01 #time discretization in s
time = 25 #time interval for time domain response in s
sensors = [0,1,0,1] #x, v, fi, omega

t = np.arange(0, time, dt) #vector of time
u = np.zeros_like(t)
u = force(t) #vector of input

Plot(
    response = Response(
        index = 0,
        modelfilter= KalmanFilter(
            model = Sensors(
                C = sensors,
                model = Disturbances(
                    covarianceDist = Vd,
                    covarianceNoise = Vn,
                    daug = D,
                    inputSignal = ModelInput(
                        loadIndex = 1,
                        dt = dt,
                        u = u,
                        model = StateSpaceModel(
                            mass = m,
                            trolleyMass = M,
                            length = L,
                            g = g
                        ),
                    )
                )
            )
        )
    )
).Show()