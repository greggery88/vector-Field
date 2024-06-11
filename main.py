import matplotlib.pyplot as plt
import numpy as np

# universal constants
e = 1.6 * 10**-19
k = 8.99 * 10**17

ax = plt.figure().add_subplot(projection="3d")


class Particle:

    def __init__(self, px, py, pz):
        vx, vy, vz = 0, 0, 0
        self.velocity = np.array([vx, vy, vz])
        self.pos = np.array([px, py, pz])
        self.Q = 1 * e

    def update(self, p_l):
        for particle in p_l:
            p = particle
            r = (p.pos - self.pos)
            r_mag = (r[0]**2 + r[1]**2 + r[2]**2) ** 1/2
            p_u, p_v, p_w = ((k * p.Q * self.Q * r) / r_mag**3)
            velo_to_p = np.array([p_u, p_v, p_w])
            self.velocity + velo_to_p + self.velocity

        self.pos += self.velocity



def vector_finder(particles, x, y, z):
    u, v, w = 0, 0, 0
    for particle in particles:
        p_x = particle.pos[0]
        p_y = particle.pos[1]
        p_z = particle.pos[2]
        ax.scatter(p_x, p_y, p_z)

        u_, v_, w_ = (k * particle.Q * np.array([x - p_x, y - p_y, z - p_y])) / (
                (x - p_x)**2 + (y - p_y)**2 + (z - p_z)**2
                                                                                ) ** (3 / 2)

        u += u_
        v += v_
        w += w_

    return u, v, w


def main():
    p1 = Particle(-5, 0, 0)
    p1.charge = 1 * e
    p2 = Particle(5, 0, 0)

    p_list = [p1, p2]

    x = np.linspace(-10, 10, 11)
    y = np.linspace(-10, 10, 11)
    z = np.linspace(-10, 10, 11)
    (x, y, z) = np.meshgrid(x, y, z)
    running = True
    while running:
        for particle in p_list:
            particle.update(p_list)
            p_x = particle.pos[0]
            p_y = particle.pos[1]
            p_z = particle.pos[2]
            ax.scatter(p_x, p_y, p_z)

        u, v, w = vector_finder(p_list, x, y, z)

        ax.quiver(x, y, z, u, v, w, normalize=True)
        plt.show()


if __name__ == "__main__":
    main()
