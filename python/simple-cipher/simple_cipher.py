import random
import string


class Cipher:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = self._generate_key

    @property
    def _generate_key(self):
        return "".join(random.sample(string.ascii_lowercase, 10))

    def _key_movements(self):

        if self.key:
            key_movements = []

            for letter in self.key:
                key_movements.append((ord(letter) - ord("a")) % 26)

        return key_movements

    def encode(self, text):

        result = ""

        for index, letter in enumerate(text):
            movement = 0
            key_movements = self._key_movements()
            movement = index % len(self.key)
            result += chr(
                (ord(letter) - ord("a") + key_movements[movement]) % 26 + ord("a")
            )

        return result

    def decode(self, text):
        result = ""

        for index, letter in enumerate(text):
            movement = 0
            key_movements = self._key_movements()
            movement = index % len(self.key)
            result += chr(
                (ord(letter) - ord("a") - key_movements[movement]) % 26 + ord("a")
            )

        return result
