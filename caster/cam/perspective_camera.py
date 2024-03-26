import numpy as np
from caster.geometry.ray import Ray

class PerspectiveCamera:
    def __init__(self, center, direction, up, angle):
        self.center = np.array(center)
        self.direction = np.array(direction)
        self.up = np.array(up)
        self.angle = angle

    def generate_ray(self, x, y):
        aspect_ratio = 1.0  # Assuming square pixels
        half_height = np.tan(np.radians(self.angle / 2))
        half_width = aspect_ratio * half_height
        u = half_width * (2 * x - 1)
        v = half_height * (2 * y - 1)

        horizontal = np.cross(self.direction, self.up)
        vertical = np.cross(horizontal, self.direction)

        direction = (self.direction + u * horizontal + v * vertical)
        return Ray(self.center, direction)
