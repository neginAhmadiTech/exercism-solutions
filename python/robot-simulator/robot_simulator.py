EAST = 2
NORTH = 1
WEST = 4
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def handle_right(self):
        if self.direction == 4:
            self.direction = 1
            return

        self.direction += 1

    def handle_left(self):
        if self.direction == 1:
            self.direction = 4
            return

        self.direction -= 1

    def handle_advance(self):
        self.coordinates = list(self.coordinates)

        match (self.direction):
            case 1:
                self.coordinates[1] += 1
            case 2:
                self.coordinates[0] += 1
            case 3:
                self.coordinates[1] -= 1
            case 4:
                self.coordinates[0] -= 1

        self.coordinates = tuple(self.coordinates)

    def move(self, movements):

        for movement in movements:

            match (movement):
                case "L":
                    self.handle_left()
                case "R":
                    self.handle_right()
                case "A":
                    self.handle_advance()
