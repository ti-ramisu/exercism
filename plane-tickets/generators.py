"""Functions to automate Conda airlines ticketing system."""
seat_letters = ['A', 'B', 'C', 'D']

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    for i in range(number):
        yield seat_letters[i % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    # Create a generator for seat letters
    seat_letter_gen = generate_seat_letters(number)
    
    for i in range(number):
        # Calculate row number (starting from 1, 4 seats per row)
        row = (i // 4) + 1
        
        # Skip row 13
        if row >= 13:
            row += 1
            
        # Get seat letter from the generate_seat_letters function
        seat_letter = next(seat_letter_gen)
        
        yield f'{row}{seat_letter}'

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passenger_seat_gen = generate_seats(len(passengers))
    seat_assigner = {}

    for passenger in passengers:

        passenger_seat = next(passenger_seat_gen)
        seat_assigner[passenger] = passenger_seat

    return seat_assigner


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        code = f'{seat}{flight_id}'
        yield code.ljust(12, '0')
