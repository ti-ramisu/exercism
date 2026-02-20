def steps(number):
    sequence = []

    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number*3 + 1
        sequence.append(number)
    return len(sequence)