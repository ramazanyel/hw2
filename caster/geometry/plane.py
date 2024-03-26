import numpy as np
from caster.geometry.object3d import Object3D
from caster.geometry.hit import Hit

class Plane(Object3D):
    def __init__(self, normal, d, color):
        super().__init__(color)
        self.normal = np.array(normal)
        self.d = d

    def intersect(self, ray, hit, tmin):
        denom = np.dot(ray.direction, self.normal)
        if abs(denom) > 1e-6:
            t = (self.d - np.dot(ray.origin, self.normal)) / denom
            if t > tmin and t < hit.t:
                hit.t = t
                hit.color = self.color
                hit.normal = self.normal / np.linalg.norm(self.normal)
                return True
        return False
