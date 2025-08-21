def equilateral(sides):
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]


def scalene(sides):
    if not is_triangle(sides):
        return False
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]


def is_triangle(sides):
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False

    return a + b >= c and b + c >= a and c + a >= b
