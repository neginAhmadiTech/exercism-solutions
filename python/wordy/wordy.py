"""Module to calculate basic math equations
based on the simple math word problems
"""

OPERATIONS = ["plus", "minus", "divided", "multiplied"]

def answer(question):
    """calculate basic math equations
    based on the simple math word problems

    Args:
        question (str): The given math str

    Returns:
        int: The result of the calculation
    """

    if not question.startswith("What is") and not question.endswith("?"):
        raise ValueError("syntax error")

    question = question.replace("What is", "")
    question = question.replace("?", "")
    question = question.replace(" by", "").strip()
    question = question.split(" ")


    result = 0
    try:
        result = int(question[0])
        question.pop(0)

        if len(question) == 1:
            if question[0] not in OPERATIONS:
                raise ValueError("unknown operation")

        if len(question) % 2 != 0:
            raise ValueError("syntax error")

        while len(question) > 0:

            operation = question.pop(0)

            number = 0
            if len(question) > 0:
                number = int(question.pop(0))


            if operation == "plus":
                result += number

            elif operation == "minus":
                result -= number

            elif operation == "multiplied":
                result *= number

            elif operation == "divided":
                result //= number

            else:
                raise ValueError("unknown operation")

        return result

    except ValueError as error:
        if str(error) == "unknown operation":
            raise error
        raise ValueError("syntax error") from error
