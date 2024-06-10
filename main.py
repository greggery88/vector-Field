import matplotlib.pyplot as plt
import numpy as np

# universal constants
e = 1.6 * 10**-19
k = 8.99 * 10**17

ax = plt.figure().add_subplot(projection="3d")


class Particle:

    def __init__(self, px, py, pz):
        self.position = np.array([px, py, pz])
        self.charge = 1 * e


def vector_finder(particles, x, y, z):
    u, v, w = 0, 0, 0
    for particle in particles:
        p_x = particle.position[0]
        p_y = particle.position[1]
        p_z = particle.position[2]
        ax.scatter(p_x, p_y, p_z)

        u_, v_, w_ = (k * particle.charge * np.array([x - p_x, y - p_y, z - p_z])) / (
            x**2 + y**2
        ) ** (3 / 2)

        u, v, w = u + u_, v + v_, w + w_

    print(u)

    return u, v, w


def main():
    p1 = Particle(-0.5, 0, 0)
    p1.charge = -1 * e
    p2 = Particle(0.5, 0, 0)
    p_list = [p1, p2]
    print(p_list)

    x = np.linspace(-1, 1, 6)
    y = np.linspace(-1, 1, 6)
    z = np.linspace(-1, 1, 6)
    (x, y, z) = np.meshgrid(x, y, z)

    for particle in p_list:
        p_x = particle.position[0]
        p_y = particle.position[1]
        p_z = particle.position[2]
        ax.scatter(p_x, p_y, p_z)

    u, v, w = vector_finder(p_list, x, y, z)

    ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
    plt.show()


if __name__ == "__main__":
    main()
