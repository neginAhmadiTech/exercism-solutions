import math


class Rational:
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        self.numer = numer // gcd
        self.denom = denom // gcd

        self._normalize()

    def _normalize(self):
        if self.numer < 0:
            self.numer = abs(self.numer)
            self.denom = (-1) * self.denom
        elif self.numer == 0:
            self.denom = 1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f"{self.numer}/{self.denom}"

    def __add__(self, other):
        numer = (self.numer * other.denom) + (other.numer * self.denom)
        denom = self.denom * other.denom

        return Rational(numer, denom)

    def __sub__(self, other):
        numer = (self.numer * other.denom) - (other.numer * self.denom)
        denom = self.denom * other.denom

        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom

        return Rational(numer, denom)

    def __truediv__(self, other):
        numer = other.denom
        denom = other.numer

        return self * Rational(numer, denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):

        if power < 0:
            numer = self.denom
            denom = self.numer
            return Rational(numer ** abs(power), denom ** abs(power))

        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
