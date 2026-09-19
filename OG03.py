import math

def area_by_base_height(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Основание и высота должны быть больше нуля.")
    return base * height / 2
area1 = area_by_base_height(20, 6)
print(f"Площадь по основанию и высоте: {area1}")