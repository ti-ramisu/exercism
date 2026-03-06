def convert(number):
    rain = ""
    if number % 3 == 0:
        rain += "Pling"
    if number % 5 == 0:
        rain += "Plang"
    if number % 7 == 0:
        rain += "Plong"
    return rain or f"{number}"
