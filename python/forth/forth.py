class StackUnderflowError(Exception):
    pass


def plus(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):

    if second_number == 0:
        raise ZeroDivisionError("divide by zero")

    return first_number // second_number


def swap(stack):
    second_number, first_number = stack.pop(), stack.pop()
    stack.append(second_number)
    stack.append(first_number)
    return stack


def over(stack):
    stack.append(stack[-2])

    return stack


def dup(stack):
    stack.append(stack[-1])

    return stack


def drop(stack):
    stack.pop()

    return stack


def check_word_type(word, stack):

    if word.startswith("-") and len(word) > 1:
        stack.append(int(word))

    elif word.isdigit():
        stack.append(int(word))
    elif word in BUILT_IN_MATH_OPERATIONS:
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        second_number = stack.pop()
        first_number = stack.pop()
        stack.append(BUILT_IN_MATH_OPERATIONS[word](first_number, second_number))

    elif word in BUILT_IN_STACK_COMMANDS_TWO_PROPS:
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")

        stack = BUILT_IN_STACK_COMMANDS_TWO_PROPS[word](stack)

    elif word in BUILT_IN_WORDS_ONE_PROP:
        if len(stack) < 1:
            raise StackUnderflowError("Insufficient number of items in stack")

        stack = BUILT_IN_WORDS_ONE_PROP[word](stack)

    else:
        raise ValueError("undefined operation")

    return stack


def execute_word(word, stack, user_defined_words):

    if word in user_defined_words:
        for operation in user_defined_words[word]:
            stack = execute_word(operation, stack, user_defined_words)

    else:
        stack = check_word_type(word, stack)

    return stack


BUILT_IN_STACK_COMMANDS_TWO_PROPS = {
    "SWAP": swap,
    "OVER": over,
}
BUILT_IN_MATH_OPERATIONS = {
    "+": plus,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

BUILT_IN_WORDS_ONE_PROP = {
    "DUP": dup,
    "DROP": drop,
}


def evaluate(input_data):
    user_defined_words = {}
    stack = []

    for data in input_data:
        words = data.split(" ")

        while words:
            word = words.pop(0).upper()

            if word == ":":

                key = words.pop(0).upper()
                if key.isdigit() or (key.startswith("-") and len(key) > 1):
                    raise ValueError("illegal operation")

                old_definition = user_defined_words.get(key)

                user_defined_words[key] = []

                while True:
                    word = words.pop(0).upper()

                    if word == ";":
                        break

                    # If this word is the word we're redefining,
                    # use its OLD definition.
                    if word == key:
                        user_defined_words[key].extend(old_definition)

                    # If it's another user-defined word,
                    # copy its definition as it exists NOW.
                    elif word in user_defined_words:
                        user_defined_words[key].extend(user_defined_words[word])

                    # Otherwise, store the word itself.
                    else:
                        user_defined_words[key].append(word)

            else:
                stack = execute_word(word, stack, user_defined_words)

    return stack
