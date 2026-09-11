import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.number = (real, imaginary)
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return other.real == self.real and other.imaginary == self.imaginary

    def __add__(self, other):
        if isinstance(other, int):
            return ComplexNumber(other + self.real, self.imaginary)

        return ComplexNumber(other.real + self.real, other.imaginary + self.imaginary)

    def __radd__(self, other):
        return ComplexNumber(other + self.real, self.imaginary)

    def __mul__(self, other):

        if isinstance(other, int):
            return ComplexNumber(other * self.real, other * self.imaginary)

        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)

        return ComplexNumber(real_part, imaginary_part)

    def __rmul__(self, other):
        return ComplexNumber(other * self.real, other * self.imaginary)

    def __sub__(self, other):

        if isinstance(other, int):
            return ComplexNumber(self.real - other, self.imaginary)

        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __rsub__(self, other):
        return ComplexNumber(other - self.real, (-1) * self.imaginary)

    def __truediv__(self, other):

        if isinstance(other, int):
            return ComplexNumber(self.real / other, self.imaginary / other)

        real_part = (self.real * other.real + self.imaginary * other.imaginary) / (
            other.real**2 + other.imaginary**2
        )
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / (
            other.real**2 + other.imaginary**2
        )

        return ComplexNumber(real_part, imaginary_part)

    def __rtruediv__(self, other):
        return ComplexNumber(
            other / (self.real + self.imaginary),
            other / (self.real + self.imaginary) * (-1),
        )

    def __abs__(self):
        return int((self.real**2) + (self.imaginary**2)) ** (1 / 2)

    def conjugate(self):
        return ComplexNumber(self.real, self.imaginary * (-1))

    def exp(self):
        real_part = math.e**self.real * math.cos(self.imaginary)
        imaginary_part = math.e**self.real * math.sin(self.imaginary)

        return ComplexNumber(real_part, imaginary_part)
