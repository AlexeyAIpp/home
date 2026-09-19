import math

def area_by_base_height(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Основание и высота должны быть больше нуля.")
    return base * height / 2

area1 = area_by_base_height(10, 6)
print(f"Площадь по основанию и высоте: {area1}")

def area_by_heron(a: float, b: float, c: float) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Длины сторон должны быть больше нуля.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует.")
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

area2 = area_by_heron(3, 4, 5)
print(f"Площадь по формуле Герона: {area2}")