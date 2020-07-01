# 一个简单的二维向量类
from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r, %r)'%(self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self): 
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)   

v = Vector(3,4)
print(abs(v))
print(abs(v * 3))

v1 = Vector(1,2)
v2 = Vector(3,-2)
print(v1 + v2)          # Vector(4, 0)
