import matplotlib.pyplot as plt

from Reponse import Response
class Plot:
    def __init__(self,
                 response: Response
                 ):
        self.t = response.t
        self.A = response.run()
        self.x = response.y
        self._ = response._


    def Show(self):
        x_labels = ('x', 'v', 'theta', 'omega')
        [plt.plot(self.t, self._[:, k], linewidth=1.2, label=x_labels[k]) for k in range(4)]
        plt.gca().set_prop_cycle(None)  # reset color cycle
        #[plt.plot(t, xhat[:, k], '--', linewidth=2, label=x_labels[k] + '_hat') for k in range(0, 4)]
        plt.ylim(-0.2, 0.8)
        plt.legend()
        plt.show()