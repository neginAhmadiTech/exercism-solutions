
"""Module to report the house events based
on the given start and end verse
"""
PIECES = [
    ("the house that Jack built.", ""),
    ("the malt", "that lay in"),
    ("the rat", "that ate"),
    ("the cat", "that killed"),
    ("the dog", "that worried"),
    ("the cow with the crumpled horn", "that tossed"),
    ("the maiden all forlorn", "that milked"),
    ("the man all tattered and torn", "that kissed"),
    ("the priest all shaven and shorn", "that married"),
    ("the rooster that crowed in the morn", "that woke"),
    ("the farmer sowing his corn", "that kept"),
    ("the horse and the hound and the horn", "that belonged to"),
]

def recursive_house(verse_number):
    """Function to print the recursion 
    of the house events based on the given verse

    Args:
        verse_number (int): given verse number

    Returns:
        str: the cursion of all the events 
        till the first one
    """
    subject = PIECES[verse_number][0]
    verb = PIECES[verse_number][1]
    current_piece = f"{subject} {verb} "

    if verse_number == 0:
        return f"{subject}"

    return current_piece + recursive_house(verse_number - 1)


def recite(start_verse, end_verse):
    """Function to report the house events based
        on the given start and end verse

    Args:
        start_verse (int): given start verse
        end_verse (int): given end verse

    Returns:
        str: the final report
    """

    result = []
    for verse_number in range(start_verse - 1, end_verse):
        result.append("This is " + recursive_house(verse_number))

    return result
