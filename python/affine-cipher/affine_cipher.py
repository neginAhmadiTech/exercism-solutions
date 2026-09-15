import math


def is_coprime(a):
    return math.gcd(a, 26) == 1


def encode(plain_text, a, b):

    if not is_coprime(a):
        raise ValueError("a and m must be coprime.")

    result = ""

    for letter in plain_text.lower():

        if letter in [" ", ",", "."]:
            continue

        if not "a" <= letter <= "z":
            result += letter
            continue

        letter_number_in_alphabet = (ord(letter) - ord("a")) % 26
        encoded = ord("a") + (a * letter_number_in_alphabet + b) % 26
        result += chr(encoded)

    result = " ".join([result[index : index + 5] for index in range(0, len(result), 5)])

    return result


def find_a_inverse(a):

    for x in range(26):
        if (a * x) % 26 == 1:
            return x


def decode(ciphered_text, a, b):

    if not is_coprime(a):
        raise ValueError("a and m must be coprime.")

    result = ""
    ciphered_text = ciphered_text.replace(" ", "")
    a_inverse = find_a_inverse(a)

    for letter in ciphered_text:

        if not "a" <= letter <= "z":
            result += letter
            continue

        letter_number_in_alphabet = (ord(letter) - ord("a")) % 26
        decoded = ord("a") + (a_inverse) * (letter_number_in_alphabet - b) % 26
        result += chr(decoded)

    return result
