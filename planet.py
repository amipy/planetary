import math


class Planet:
    G = 1

    def __init__(self, loc, vel, mass):
        self.position=loc
        self.velocity=vel
        self.mass=mass
    def proccessMove(self, dt):
        self.position[0]+=self.velocity[0]*dt
        self.position[1] += self.velocity[1] * dt
        #(x,y)

    def proccessVel(self, a, dt):
        self.velocity[0] += a[0]*dt
        self.velocity[1] += a[1]*dt

    @staticmethod
    def calcGravityForce(p1, p2):
        r2 = Planet.distance2(p1, p2)
        F = Planet.G * p1.mass * p2.mass / r2
        d = math.sqrt(r2)
        a = (
            (p2.position[0] - p1.position[0]) / d * F / p1.mass,
            (p2.position[1] - p1.position[1]) / d * F / p1.mass
        )
        return a

    @staticmethod
    def distance2(p1, p2):
        return (p1.position[0] - p2.position[0]) ** 2 + (p1.position[1] - p2.position[1]) ** 2