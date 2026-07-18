"""Module to find out the result of the 
tic-tac-toe game
"""
def board_full(board):
    """Checks if the board is full or not

    Args:
        board (list): The board in a list

    Returns:
        bool: The result if the board is full or not
    """

    for row in board:
        if row.count(" ") > 0:
            return False

    return True

def o_win(board):
    """Checks if 'O' player wins or not

    Args:
        board (list): The board in a list

    Returns:
        bool: The result if 'O' wins
    """

    for index, row in enumerate(board):
        if row.count("O") == 3:
            return True

        if board[0][index] == board[1][index] == board[2][index] == "O":
            return True

    if board[0][0] == board[1][1] == board[2][2] == "O":
        return True
    if board[0][2] == board[1][1] == board[2][0] == "O":
        return True

    return False

def x_win(board):
    """Checks if 'X' player wins or not

    Args:
        board (list): The board in a list

    Returns:
        bool: The result if 'X' wins
    """

    for index, row in enumerate(board):
        if row.count("X") == 3:
            return True

        if board[0][index] == board[1][index] == board[2][index] == "X":
            return True

    if board[0][0] == board[1][1] == board[2][2] == "X":
        return True
    if board[0][2] == board[1][1] == board[2][0] == "X":
        return True

    return False


def o_count(board):
    """Counts the number of 'O's in the board

    Args:
        board (list): The board in a list

    Returns:
        int: the number of 'O's
    """

    counter = 0
    for row in board:
        counter += row.count("O")

    return counter

def x_count(board):
    """Counts the number of 'X's in the board

    Args:
        board (list): The board in a list

    Returns:
        int: the number of 'X's
    """

    counter = 0
    for row in board:
        counter += row.count("X")

    return counter

def gamestate(board):
    """Finds out the game state and returns it

    Args:
        board (list): The board in a list

    Raises:
        ValueError: Raises if wrong turn order: O started
        ValueError: Raises if wrong turn order: X went twice
        ValueError: Raises if impossible board: game should have ended after the game was won

    Returns:
        str: The state of the game
    """

    if o_count(board) > x_count(board):
        raise ValueError("Wrong turn order: O started")

    if x_count(board) > o_count(board) + 1:
        raise ValueError("Wrong turn order: X went twice")

    if x_win(board) and o_win(board):
        raise ValueError("Impossible board: game should have ended after the game was won")

    if x_win(board) and x_count(board) != o_count(board) + 1:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if o_win(board) and x_count(board) != o_count(board):
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_win(board):
        if x_count(board) == o_count(board) + 1:
            return "win"


    if o_win(board):
        if x_count(board) == o_count(board):
            return "win"


    if board_full(board):
        return "draw"

    return "ongoing"
