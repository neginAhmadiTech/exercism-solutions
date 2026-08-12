"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate ):
        self.x_coordinate = x_coordinate
        self.y_coordinate  = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """Decreases the health by 1
        """
        self.health -= 1
        
    
    def is_alive(self):
        """Checks if the alien is alive using the health attribute

        Returns:
            bool: True if it's alive and false if it's not
        """
        return self.health > 0
    
    
    def teleport(self, x_coordinate, y_coordinate):
        """Updates the coordinates with the new ones

        Args:
            x_coordinate (int): the coordinate of x
            y_coordinate (int): the coordinate of y
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        
    
    def collision_detection(self, other_object):
        """This will be implemented later

        Args:
            other_object (Alien): Another alien
        """
        pass


def new_aliens_collection(alien_start_positions):
    """With the given list of positions, it returns
    back the list of aliens with that positions

    Args:
        alien_start_positions (list[tuple]): The given list of start positions

    Returns:
        list[Alien]: The list of new instances of Aliens
    """
    
    aliens = []
    for (x, y) in alien_start_positions:
        alien = Alien(x, y)
        aliens.append(alien)

    return aliens
