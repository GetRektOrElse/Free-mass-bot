from math import sin, cos, tan, asin, acos, atan, pi


def coords(center, radius, angle):
    offset = (round(radius * sin(angle), 3), round(radius * cos(angle), 3))
    return tuple(a + b for a, b in zip(center, offset))

print(coords([5, 2], 2, pi*1.5))