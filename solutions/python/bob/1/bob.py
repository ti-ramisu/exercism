def response(hey_bob):
    if not hey_bob or hey_bob.isspace():
        return "Fine. Be that way!"

    if hey_bob.rstrip()[-1] == "?":
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."

    if hey_bob.isupper():
        return "Whoa, chill out!"

    return "Whatever."
