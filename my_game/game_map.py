from helpers import log_message

# Поки що не можна створити.
# Треба змінити архітектуру програми 
class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.content = ' '

    def __repr__(self):
        return f'Cell: {self.x}, {self.y} |{self.content}|'
    
    def __str__(self):
        return f'Cell: {self.x}, {self.y} |{self.content}|'


class Map:

    def __init__(self):
        self.__n = 5
        self.__m = 5
        self.map = [[Cell(j, i) for i in range(self.__n)] for j in range(self.__m)]
        self.__current_x = 0
        self.__current_y = 0

    def __next__(self):


        if self.__current_x == self.__m:
            self.__current_x = 0
            self.__current_y += 1

            if self.__current_y == self.__n:
                raise StopIteration


        self.cell = self.map[self.__current_x][self.__current_y]
        self.cell.content = 'X'
        self.__current_x += 1
        
        return self.cell

    def __iter__(self):
        self.__current_x = 0
        self.__current_y = 0
        return self
    
    def __str__(self):
        self.my_map = ''
        self.row = '|'
        for cell in world_map:
            if self.__current_x < self.__m:
                self.row += cell.content + '|'
            if self.__current_x == self.__m - 1:
                self.my_map += self.row + '\n'
                self.row = '|'

        return self.my_map
    

def generate(obj):
    for i in obj:
        yield i

        

world_map = Map()
for cell in world_map:
    print(cell)

print(world_map)

generator = generate(world_map)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


def turns(func):

    def inner(*qrgs, **kwargs):

        func(*qrgs, **kwargs)

    return inner


def generate_map(objects, size_n, size_m):

    log_message(f'Generating map size_n: {size_n}; size_m: {size_m}')

    world_map = [[' ' for i in range(size_n)] for _ in range(size_m)]
    
    for obj in objects:
        world_map[obj.y][obj.x] = obj.sign
    
    log_message(f'Generated map size_n: {size_n}; size_m: {size_m}')

    return world_map


def print_map(world_map):

    for row in world_map:
        print(f'|{"|".join(row)}|')
