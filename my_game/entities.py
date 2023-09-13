from config import Config

# Entities - сутності 


class Movable:

    movable = True
    
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.config = Config()

        self.moves = {
        'w': self.move_up,
        's': self.move_down,
        'a': self.move_left,
        'd': self.move_right,
        'wa': self.move_up_left,
        'aw': self.move_up_left,
        }

    def move_up(self):

        if self.y > 0:
            self.y-= 1

    def move_down(self):

        if self.y < self.config.size_m - 1:
            self.y += 1

    def move_left(self):

        if self.x > 0:
            self.x -= 1

    def move_right(self):

        if self.x < self.config.size_n - 1:
            self.x += 1

    def move_up_left(self):

        if self.y > 0 and self.x > 0:
            self.x -= 1
            self.y -= 1

    def move(self, direction):
        self.moves[direction]()


class NonMovable:

    movable = False

    def __init__(self, x, y):

        self.x = x
        self.y = y


class Portal(NonMovable):

    sign = 'O'


class Enemy(Movable):

    sign = 'E'

    
class Character(Movable):

    sign = 'X'


