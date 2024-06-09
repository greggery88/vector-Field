import matplotlib.pyplot as plt
import numpy as np

# universal constants
e = 1.6 * 10**-19
k = 8.99 * 10**9

ax = plt.figure().add_subplot(projection="3d")

x = np.linspace(-1, 1, 10)

print(x)

u = 1
v = 0
w = 0


class Particle:

    def __init__(self, px, py, pz):
        self.position = np.array([px, py, pz])
        self.charge = 1 * e


def main():
    particle = Particle(0, 0, 0)
    p_x = particle.position[0]
    p_y = particle.position[1]
    p_z = particle.position[2]
    ax.scatter(p_x, p_y, p_z)
    ax.quiver(x, y, z, u, v, w, length=0.1)
    plt.show()


if __name__ == "__main__":
    main()
