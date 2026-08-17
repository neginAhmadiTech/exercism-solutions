NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4
DIRECTION_MOVEMENT = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0),
}
RIGHT = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH,
}
LEFT = {
    NORTH: WEST,
    WEST: SOUTH,
    SOUTH: EAST,
    EAST: NORTH,
}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def handle_advance(self):

        x, y = self.coordinates
        x_movement, y_movement = DIRECTION_MOVEMENT[self.direction]
        self.coordinates = (x + x_movement, y + y_movement)

    def move(self, movements):

        for movement in movements:

            match (movement):
                case "L":
                    self.direction = LEFT[self.direction]
                case "R":
                    self.direction = RIGHT[self.direction]
                case "A":
                    self.handle_advance()
