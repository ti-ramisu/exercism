def score(x, y):
    # using distance equation (x-0)^2+(y-0)^2 < radius^2
    # 0 because circle centred at 0
    dx = abs(x) ** 2
    dy = abs(y) ** 2

    if 5 ** 2 < dx + dy <= 10 ** 2:
        return 1
    elif 1 < dx + dy <= 5 ** 2:
        return 5
    elif 0 <= dx + dy <= 1:
        return 10

    return 0
d