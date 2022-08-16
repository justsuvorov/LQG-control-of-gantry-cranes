import numpy as np
from ModelInput import ModelInput
from Disturbances import Disturbances
from response_result import ResponseResult
class Sensors():
    """
    Build matrix C for a state-space representation of a gantry crane linear system.

    x' = Ax + Bu
    y = Cx + Du

    Parameters
    ----------

    Inputs:
    C : vector of mesuarments (where are sensors) [x, v, fi, omega]
    model : StateSpaceModel with matrices A, B, C, D

    Returns
    -------
    Modelbuilder : Matrix  C

    See Also https://en.wikipedia.org/wiki/State-space_representation
    -------

    """
    def __init__(self,
        C : [],
        model: Disturbances,
    ):
        self._cSensors = np.array(C)
        self.model = model
        self.t = []

    def builder(self):
        result = self.model.builder()
        Cc = self._cSensors
        return ResponseResult(A = result.A,
                              B = result.B,
                              C = Cc,
                              D = result.D,
                              U = result.U,
                              Vn = result.Vn,
                              t = result.t,
                              Vd = result.Vd)