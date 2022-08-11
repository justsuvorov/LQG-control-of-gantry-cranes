import control
import control.matlab
from Sensors import Sensors

class KalmanFilter:
    def __init__(self,
                 model: Sensors

                 ):
        self.Vn = model.noise
