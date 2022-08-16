from StateSpaceModel import StateSpaceModel
from ModelInput import ModelInput
import numpy as np
from Disturbances import Disturbances
from Sensors import Sensors
from Reponse import Response
from KalmanFilter import KalmanFilter
from Plot import Plot

def Force(t):
    F = 59.5394 * np.exp(-247.492 * t) - 365.263* np.exp(-50. * t) + \
        47.2495 * np.exp(-7.39438 * t) + (99.4454 -
    201.182 *  1j) * np.exp((-5.61451 - 4.92613 * 1j) * t) + (99.4454 +
    201.182 * 1j ) * np.exp((-5.61451 + 4.92613 * 1j) * t) + 59.5829 * np.exp(-1.33333 * t)
    return F.real

#Параметры системы
m = 15
M = 80
L = 1.15
g = -10
Vd = 0.00001  # distrubance covariance
Vn = 0.01  # noise covariance
D= [0, 0, 1, 1, 1, 1]  # D matrix passes noise and disturbances through [F,x,v,fi,omega,y]
dt = 0.01
time = 25
t = np.arange(0, time, dt)
u = np.zeros_like(t)
u = Force(t)
C = [1,0,0,0]
sensors = [0,1,0,1] #x, v, fi, omega

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
                            length = L
                        ),
                    )
                )
            )
        )
    )
).Show()