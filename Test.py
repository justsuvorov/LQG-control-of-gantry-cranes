from StateSpaceModel import StateSpaceModel
from ModelInput import ModelInput
import numpy as np
from Disturbances import Disturbances
from Sensors import Sensors
from Reponse import Response
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
Vd = 0.00005  # distrubance covariance
Vn = 0.001  # noise covariance
D= [0, 0, 1, 1, 1, 1]  # D matrix passes noise and disturbances through [F,x,v,fi,omega,y]
dt = 0.01
time = 25
t = np.arange(0, time, dt)
u = np.zeros_like(t)
u = Force(t)
C = [1,0,0,0]
"""
crane = StateSpaceModel(m, M, L)

input = ModelInput(1, dt, crane, u = u, )

disturbances = Disturbances(Vd, Vn, D, input)

sensors = Sensors(C,disturbances)

response = Response(0, sensors)
"""
Plot(
    response = Response(
        index = 0, 
        model = Sensors(
            C = C,
            model = Disturbances(
                covarianceDist = Vd, 
                covarianceNoise = Vn, 
                daug = D,
                inputSignal= ModelInput(
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
).Show()


#Plot(response).Show()










