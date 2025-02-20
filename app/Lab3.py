from math import pi


def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")


def trapezium_area(a, b, h):
    if all(isinstance(x, (int, float)) and x >= 0 for x in [a, b, h]):
        return 0.5 * (a + b) * h
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")


def ellipse_area(a, b):
    if all(isinstance(x, (int, float)) and x >= 0 for x in [a, b]):
        return pi * a * b
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")


def rhombus_area(d1, d2):
    if all(isinstance(x, (int, float)) and x >= 0 for x in [d1, d2]):
        return 0.5 * d1 * d2
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

