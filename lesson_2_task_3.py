import math

def square(side):
    area = side * side
    if not isinstance(area, int):
        area = math.ceil(area)
    return area

side = 6
area = square(side)
print(f"Площадь квадрата со стороной {side} равна {area}")