import math

def area_by_heron(a: float, b: float, c: float) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Длины сторон должны быть больше нуля.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует.")
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

area2 = area_by_heron(3, 4, 5)
print(f"Площадь по формуле Герона: {area2}")