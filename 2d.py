import logging

import numpy as np
import matplotlib.pyplot as plt

ax = plt.figure().add_subplot()
k = 8.99 * 10 ** 9

log = logging.getLogger(__name__)


def draw(x, y):
    ax.scatter(x, y)


class Particle:
    def __init__(self, px, py, pu=0, pv=0):

        self.pos = np.array([px, py])
        self.V = np.array([0, 0])
        self.a = np.array([pu, pv])
        self.Q = 1.6 * 10 ** -19

    def update_accel(self, p_list):
        for particle in p_list:
            if particle is not self:
                r = particle.pos - self.pos
                #
                r_mag = np.linalg.norm(r)
                r_hat = r / r_mag

                a = (k * self.Q * particle.Q) / r_mag ** 2 * r_hat
                self.a = a + self.a
                print(self.a)

    def update_pos(self):
        self.V = self.V + self.a
        self.pos = self.pos + self.V


# words

def main():
    logging.basicConfig(level=logging.INFO)
    p1 = Particle(0, 0)
    p2 = Particle(1, 0)

    running = True
    while running:

        for particle in [p1, p2]:
            x, y = particle.pos
            particle.update_accel([p1, p2])
            particle.update_pos()
            particle.draw(x, y)

            u, v = particle.V
            log.info(u)
            log.info(v)

            ax.quiver(x, y, u, v)
        plt.show()


main()
