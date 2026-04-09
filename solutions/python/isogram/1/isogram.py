def is_isogram(string):
    string = string.lower()
    string_alpha = "".join(x for x in string if x.isalpha())
    unique_chars = set()

    for char in string_alpha:
        if char in unique_chars:
            return False

        else:
            unique_chars.add(char)
        print(unique_chars)
    return True
