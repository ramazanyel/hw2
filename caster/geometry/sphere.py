import numpy as np
from geometry.object3d import Object3D
from geometry.ray import Ray
from geometry.hit import Hit

class Sphere(Object3D):
    def __init__(self, center, radius, color):
        super().__init__(color)
        self.center = np.array(center)
        self.radius = radius

    def intersect(self, ray, hit, tmin):
        oc = ray.origin - self.center
        a = np.dot(ray.direction, ray.direction)
        b = 2.0 * np.dot(oc, ray.direction)
        c = np.dot(oc, oc) - self.radius**2

        discriminant = b**2 - 4 * a * c

        if discriminant > 0:
            t1 = (-b - discriminant**0.5) / (2.0 * a)
            t2 = (-b + discriminant**0.5) / (2.0 * a)

            if tmin < t1 < hit.t:
                hit.t = t1
                hit.color = self.color
            elif tmin < t2 < hit.t:
                hit.t = t2
                hit.color = self.color
