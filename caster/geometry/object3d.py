from abc import ABC, abstractmethod

class Object3D(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def intersect(self, ray, hit, tmin):
        pass
