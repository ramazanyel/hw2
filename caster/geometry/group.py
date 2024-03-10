
from geometry.object3d import Object3D
from geometry.hit import Hit

class Group(Object3D):
    def __init__(self, objects):
        super().__init__((0, 0, 0))  # Group color is not used
        self.objects = objects

    def intersect(self, ray, hit, tmin):
        for obj in self.objects:
            obj.intersect(ray, hit, tmin)
