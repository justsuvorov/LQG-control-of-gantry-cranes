import numpy as np
from ModelInput import ModelInput
from Disturbances import Disturbances
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
        vD = model.Vd
        noise = model.Vn
        Cc = self._cSensors
        A, B, C, D, U = self.model.builder()
        self.t = self.model.t
        return A, B, Cc, D, U#, noise, vD