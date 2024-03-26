# geometry/transformation.py
import numpy as np
from caster.geometry.object3d import Object3D
from caster.geometry.hit import Hit

class Transformation(Object3D):
    def __init__(self, m, obj):
        super().__init__((0, 0, 0))  # Transformation color is not used
        self.m = np.array(m)
        self.obj = obj

    def intersect(self, ray, hit, tmin):
        # Transform ray origin and direction
        transformed_ray_origin = np.dot(np.linalg.inv(self.m), np.append(ray.origin, 1))[:3]
        transformed_ray_direction = np.dot(np.linalg.inv(self.m)[:3, :3], ray.direction)

        transformed_ray = Ray(transformed_ray_origin, transformed_ray_direction)
        self.obj.intersect(transformed_ray, hit, tmin)
