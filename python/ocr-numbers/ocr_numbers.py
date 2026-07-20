
"""Module to convert a list of OCR numbers into real numbers
"""
DIGITS = [
     [
        " _ ",
        "| |",
        "|_|",
        "   "
    ],

     [
        "   ",
        "  |",
        "  |",
        "   "
        ],

     [
        " _ ",
        " _|",
        "|_ ",
        "   "
        ],

     [
        " _ ",
        " _|",
        " _|",
        "   "
        ],

     [
        "   ",
        "|_|",
        "  |",
        "   "
        ],

     [
        " _ ",
        "|_ ",
        " _|",
        "   "
        ],

     [
        " _ ",
        "|_ ",
        "|_|",
        "   "
        ],

     [
        " _ ",
        "  |",
        "  |",
        "   "
        ],

     [
        " _ ",
        "|_|",
        "|_|",
        "   "
        ]
    ,
     [
        " _ ",
        "|_|",
        " _|",
        "   "
        ]
]

def convert(input_grid):
    """Function to convert a list of OCR numbers into real numbers

    Args:
        input_grid (list): list of numbers in OCR format

    Raises:
        ValueError: Raises if number of input lines is not a multiple of four
        ValueError: Raises if number of input columns is not a multiple of three

    Returns:
        str: The converted numbers
    """

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    result = ""
    input_grid_changed = []
    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

        columns = [row[i:i+3] for i in range(0, len(row), 3)]
        input_grid_changed.append(columns)



    digit = []
    digits = []
    for row_start in range(0, len(input_grid_changed), 4):
        block = input_grid_changed[row_start:row_start + 4]

        for col_index in range(len(block[0])):
            digit = []

            for row in block:
                digit.append(row[col_index])

            digits.append(digit)

        if row_start + 4 != len(input_grid_changed) and (row_start) % 4 == 0:
            digits.append([","])


    for item in digits:
        if item in DIGITS:
            result += str(DIGITS.index(item))
        elif item == [","]:
            result += item[0]
        else:
            result += "?"

    return result
