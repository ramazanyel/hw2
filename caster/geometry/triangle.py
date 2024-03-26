import numpy as np
from caster.geometry.object3d import Object3D
from caster.geometry.hit import Hit

class Triangle(Object3D):
    def __init__(self, v1, v2, v3, color):
        super().__init__(color)
        self.v1 = np.array(v1)
        self.v2 = np.array(v2)
        self.v3 = np.array(v3)

    def intersect(self, ray, hit, tmin):
        v1v2 = self.v2 - self.v1
        v1v3 = self.v3 - self.v1
        pvec = np.cross(ray.direction, v1v3)
        det = np.dot(v1v2, pvec)

        if abs(det) < 1e-8:
            return False

        invDet = 1.0 / det
        tvec = ray.origin - self.v1
        u = np.dot(tvec, pvec) * invDet
        if u < 0 or u > 1:
            return False

        qvec = np.cross(tvec, v1v2)
        v = np.dot(ray.direction, qvec) * invDet
        if v < 0 or u + v > 1:
            return False

        t = np.dot(v1v3, qvec) * invDet

        if t < tmin or t >= hit.t:
            return False

        hit.t = t
        hit.color = self.color

        edge1 = self.v2 - self.v1
        edge2 = self.v3 - self.v1
        hit.normal = np.cross(edge1, edge2)
        hit.normal = hit.normal / np.linalg.norm(hit.normal)

        return True
