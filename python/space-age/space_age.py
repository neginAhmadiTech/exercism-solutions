"""Module with one class to convert a given age
in seconds into planets ages
"""
class SpaceAge:
    """Class to calculate the given age in seconds 
    into ages in different planets
    """

    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        """Calculate the age on earth

        Returns:
            float: calculated age on earth with 2 floating points
        """
        return round(self.seconds / 31557600, 2)

    def on_mercury(self):
        """Calculate the age on mercury

        Returns:
            float: calculated age on mercury with 2 floating points
        """
        return round(self.on_earth() / 0.2408467, 2)

    def on_venus(self):
        """Calculate the age on venus

        Returns:
            float: calculated age on venus with 2 floating points
        """
        return round(self.seconds / 31557600 / 0.61519726, 2)

    def on_mars(self):
        """Calculate the age on mars

        Returns:
            _type_: calculated age on mars with 2 floating points
        """
        return round(self.on_earth() / 1.8808158, 2)

    def on_jupiter(self):
        """Calculate the age on jupiter

        Returns:
            float: calculated age on jupiter with 2 floating points
        """
        return round(self.on_earth() / 11.862615, 2)

    def on_saturn(self):
        """Calculate the age on saturn

        Returns:
            float: calculated age on saturn with 2 floating points
        """
        return round(self.on_earth() / 29.447498, 2)

    def on_uranus(self):
        """Calculate the age on uranus

        Returns:
            float: calculated age on uranus with 2 floating points
        """
        return round(self.on_earth() / 84.016846, 2)

    def on_neptune(self):
        """Calculate the age on neptune

        Returns:
            float: calculated age on neptune with 2 floating points
        """
        return round(self.on_earth() / 164.79132, 2)
