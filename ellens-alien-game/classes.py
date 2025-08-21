"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        # decrease alien health by 1, but don't go below 0
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        pass


def new_aliens_collection(start_positions):
    alien_positions = []
    for position in start_positions:
        alien_positions.append(Alien(position[0], position[1]))
    return aliens


alien_start_positions = [(1, 2), (3, 4), (4, 7), (2, 5)]
aliens = new_aliens_collection(alien_start_positions)
for alien in aliens:
    print((alien.x_coordinate, alien.y_coordinate))
