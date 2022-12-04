class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return self.x, self.y, self.z
    def __add__(self, other):
        return self.x+self.y+self.z
    def __sub__(self, other):
        return self.x - self.y - self.z
    def __mul__(self, other):
        return self.x * self.y * self.z

f1=Vector3D(1, 2, 3)
f1.__str__()
f1.__add__()
f1.__sub__()
f1.__mul__()