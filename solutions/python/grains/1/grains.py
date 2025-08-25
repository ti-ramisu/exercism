def square(number):
    """Return grains on the given square (1..64), doubling each time."""
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Return the total number of grains on the board."""
    grains = 0
    for i in range(1, 65):
        grains += square(i)
    return grains
