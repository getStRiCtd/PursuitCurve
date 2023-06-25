import matplotlib.pyplot as plt
import numpy as np


class Plot:
    """
    Plot class for 'Chaser' and 'Victim'
    *if x == 0 than object is Victim
    *if x !=  than object is Chaser
    """

    def __init__(self, x, y, speed: int):
        self.x = x
        self.y = y
        self.speed = speed


def find_path(victim: Plot, chaser: Plot):
    xd = np.arange(-1, 2, 0.001)
    k = victim.speed / chaser.speed
    if k != 1:
        y = np.array(
            list([0.5 * (((x ** (k + 1)) / (k + 1)) - ((x ** (1 - k)) / (1 - k))) + chaser.y - 0.5 *
                  (((chaser.x ** (k + 1)) * (1 - k) - (chaser.x ** (1 - k)) * (k + 1)) / ((k + 1) * (1 - k)))]
                 for x in xd))

    else:
        y = np.array(
            list([
                     x ** 2 / 4 - 0.5 * np.log(x) + chaser.y - chaser.x ** 2 / 4 + 0.5 * np.log(chaser.x)
                 ] for x in xd)
        )
    plt.plot(xd, y)


if __name__ == "__main__":
    a = Plot(0, 0, 5)
    p = Plot(1, 0, 5)
    plt.axis([-1, p.x, 0, 10])
    find_path(a, p)
    plt.show()
