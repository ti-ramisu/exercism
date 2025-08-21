"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    
    return remaining_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

        :param number of layers: int - lasagna layers
        :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

        Function that takes the time taken to prepare a lasagna based on its layers.
        """
    return PREPARATION_TIME * number_of_layers
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

        :param number_of_layers: int - number of lasagna layers
        :param elapsed_bake_time - remaining bake time (in minutes)
        :return: int - elapsed_time_in_minutes

        Function that takes the total time left by summing preparation_time_in_minutes and
        elapsed_bake_time
        """
    y = preparation_time_in_minutes(number_of_layers) + bake_time_remaining(elapsed_bake_time)
    return y
# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

print(preparation_time_in_minutes(2))
print(bake_time_remaining(7))
print(elapsed_time_in_minutes(2,7))