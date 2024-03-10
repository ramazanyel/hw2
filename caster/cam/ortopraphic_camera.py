from cam.camera import Camera



import numpy as np
from geometry.ray import Ray


class OrthographicCamera(Camera):
    def __init__(self, center, direction, up, size):
        self.center = np.array(center)
        self.direction = np.array(direction)
        self.up = np.array(up)
        self.size = size

    def generate_ray(self, x, y):
        horizontal = np.cross(self.direction, self.up)
        origin = self.center + (x - 0.5) * self.size * horizontal + (y - 0.5) * self.size * self.up
        return Ray(origin, self.direction)