"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    seat_letters = ["A", "B", "C", "D"]
    
    for item in range(number):
        match (item % 4):
            case 0:
                yield seat_letters[0] 
            case 1:
                yield seat_letters[1]
            case 2:
                yield seat_letters[2]  
            case 3:
                yield seat_letters[3] 
    

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    seat_letters = ["A", "B", "C", "D"]
    rows = number // 4
    remainder = number % 4
    
    if rows > 12:
        rows += 1
        
    for row in range(rows):    
        
        if row == 12:
            continue
                
        yield str(row + 1) + seat_letters[0] 
        yield str(row + 1) + seat_letters[1]
        yield str(row + 1) + seat_letters[2]  
        yield str(row + 1) + seat_letters[3] 
        
        
    for item in range(remainder):
        yield str(rows + 1) + seat_letters[item]
    


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = list(generate_seats(len(passengers)))
    
    return dict(zip(passengers, seats))


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        yield seat + flight_id + (12 - (len(seat) + len(flight_id))) * "0"
