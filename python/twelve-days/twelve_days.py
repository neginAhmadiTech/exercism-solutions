"""Module to print verses from twelve days song
    based on the given start and end verse 
"""
def recite(start_verse, end_verse):
    """Function to print verses from twelve days song
    based on the given start and end verse

    Args:
        start_verse (int): Given start verse
        end_verse (int): Given end verse

    Returns:
        list: The list of the verses produced
    """
    
    days = [
        ("first", "a Partridge in a Pear Tree."),
        ("second", "two Turtle Doves, "),
        ("third", "three French Hens, "),
        ("fourth", "four Calling Birds, "),
        ("fifth", "five Gold Rings, "),
        ("sixth", "six Geese-a-Laying, "),
        ("seventh", "seven Swans-a-Swimming, "),
        ("eighth", "eight Maids-a-Milking, "),
        ("ninth", "nine Ladies Dancing, "),
        ("tenth", "ten Lords-a-Leaping, "),
        ("eleventh", "eleven Pipers Piping, "),
        ("twelfth", "twelve Drummers Drumming, "),
    ]
    
    verses = [[]]
    for gift in range(start_verse, 0, -1):
        verses[0].append(days[gift-1][1])
    
        
    for verse in range(start_verse + 1, end_verse + 1):
        last_verse = verses[-1].copy()
        # print(last_verse)
        if len(last_verse) > 1:
            verses[-1][-1] = "and " + verses[-1][-1]

        last_verse.insert(0, days[verse-1][1])
        verses.append(last_verse)
    
    if len(verses[-1]) > 1:
        verses[-1][-1] = "and " + verses[-1][-1]        
    
    day = start_verse
    result = []
    for verse in verses:
        first_sentence = f"On the {days[day-1][0]} day of Christmas my true love gave to me: "
        verse.insert(0, first_sentence)
        final_verse = "".join(verse)
        result.append(final_verse)
        day += 1

    return result
