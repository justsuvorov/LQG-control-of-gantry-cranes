import matplotlib.pyplot as plt

from Reponse import Response
class Plot:
    def __init__(self,
        response: Response
    ):
        self._response = response

    def Show(self):
        responseResult = self._response.run()
        t = responseResult.t
        x = responseResult.y
        _ = responseResult._
        x_labels = ('x', 'v', 'theta', 'omega')
        [plt.plot(t, _[:, k], linewidth=1.2, label=x_labels[k]) for k in range(4)]
        plt.gca().set_prop_cycle(None)  # reset color cycle
        #[plt.plot(t, xhat[:, k], '--', linewidth=2, label=x_labels[k] + '_hat') for k in range(0, 4)]
        plt.ylim(-0.2, 0.8)
        plt.legend()
        plt.show()