import math

number = 9

def digits(n=number):
    if n < 0:
        yield '-'
        n = -1 * n
    elif n == 0:
        yield 0
        return
    xp = int(math.log(n, 10).real)
    factor = 10 ** xp
    while n:
        yield int(n / factor)
        n = n % factor
        try:
            xp, old_xp = int(math.log(n, 10).real), xp
        except ValueError:
            for _ in range(xp):
                yield 0
            return
        factor = 10 ** xp
        for _ in range(1, old_xp - xp):
            yield 0


def is_armstrong_number(number):
    if number > 0:
        exponent = int(math.log10(number)) + 1
    if number == 0:
        exponent = 1

    total = 0
    for x in digits(number):
        add = x ** exponent
        total += add

    return total == number

is_armstrong_number(number)