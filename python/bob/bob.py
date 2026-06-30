"""
Bob is a lackadaisical teenager. In conversation, his responses are very limited.
Bob answers 'Sure.' if you ask him a question.
He answers 'Whoa, chill out!' if you yell at him (ALL CAPS).
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else.
Bob's conversational partner is a purist when it comes to written communication and always follows normal rules of grammar and punctuation in English.
"""
def response(hey_bob):
    """
    Returns the appropriate response for a given message.
    """
    trimmed = hey_bob.strip()
    message = ""
    if trimmed == "":
        message = "Fine. Be that way!"
    elif trimmed.isupper() and trimmed.endswith("?"):
        message = "Calm down, I know what I'm doing!"
    elif trimmed.isupper():
        message = "Whoa, chill out!"
    elif trimmed.endswith("?"):
        message = "Sure."
    else:
        message = "Whatever."
    return message
