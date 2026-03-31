def is_pangram(sentence):

    # Convert to lowercase and create set of alphabetic characters
    alphabet_set = set(char.lower() for char in sentence if char.isalpha())

    # Check if all 26 letters are present
    return len(alphabet_set) == 26
