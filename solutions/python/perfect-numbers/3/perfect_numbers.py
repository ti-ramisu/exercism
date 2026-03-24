def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot = set()
    for n in range(1, number):
        if number % n == 0:
            aliquot.add(n)
    aliquot_sum = sum(aliquot)

    if number == aliquot_sum:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    if number > aliquot_sum:
        return "deficient"
    return None




