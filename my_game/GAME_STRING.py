# | | | |O| |
# | | | | | |
# | | | | | |
# | |X| | | |

from random import randint, choice

# from game_engine.map import generate_map, print_map
from game_map import generate_map, print_map
# from game_engine.tools import load, save
from tools import load, save

def generate_enemies(count):

    enemies = []

    for _ in range(count):

        enemy = {'x': randint(0, SIZE_N - 1),
            'y': randint(0, SIZE_M - 1),
            'sign': 'E',
            'type': 'enemy',
            'movable': True
        }
        
        enemies. append(enemy)

    return enemies


is_load = input('Do you want to load game? (y/''): ')

if is_load.casefold() == 'y':
    objects, turns, SIZE_N, SIZE_M = load()
else:
    # SIZE_N = 30 # randint(10, 20) # column
    SIZE_N = randint(5, 10) # column

    # SIZE_M = 13 # randint(10, 20) # row
    SIZE_M = randint(5, 10) # row

    char = {'x': randint(0, SIZE_N - 1),
            'y': randint(0, SIZE_M - 1),
            'sign': 'X',
            'type': 'char',
            'movable': True
    }

    portal = {'x': randint(0, SIZE_N - 1),
              'y': randint(0, SIZE_M - 1),
              'sign': 'O',
              'type': 'portal',
              'movable': False
    }

    enemies = generate_enemies(5)

    objects = [char, portal] + enemies

    turns = 0


def check_state(objects):

    for obj in objects:

        if obj['type'] == 'char':
            char  = obj
        elif obj['type'] =='portal':
            portal = obj
        elif obj['type'] == 'enemy':
            loss_condition = char['x'] == obj['x'] and \
                            char['y'] == obj['y']
            
            if loss_condition:
                char['sign'] = 'L'
                print(f'You LOST in {turns} turns')
                break

    win_condition = char['x'] == portal['x'] and \
                    char['y'] == portal['y']
    
    if win_condition:
        char['sign'] = 'W'
        print(f'You WON in {turns} turns')        

    return win_condition or loss_condition


# def move(direction, obj, size_n=SIZE_N, size_m=SIZE_M):
    
#     if direction == 'w' and obj['y'] > 0:
#         obj['y'] -= 1
#     elif direction == 's' and obj['y'] < size_m - 1:
#         obj['y'] += 1
#     elif direction == 'a' and obj['x'] > 0:
#         obj['x'] -= 1
#     elif direction == 'd' and obj['x'] < size_n - 1:
#         obj['x'] += 1


def move_up(obj, size_n=SIZE_N, size_m=SIZE_M):

    if obj['y'] > 0:
        obj['y'] -= 1


def move_down(obj, size_n=SIZE_N, size_m=SIZE_M):

    if obj['y'] < size_m - 1:
        obj['y'] += 1


def move_left(obj, size_n=SIZE_N, size_m=SIZE_M):

    if obj['x'] > 0:
        obj['x'] -= 1


def move_right(obj, size_n=SIZE_N, size_m=SIZE_M):

    if obj['x'] < size_n - 1:
        obj['x'] += 1


def move_up_left(obj, size_n=SIZE_N, size_m=SIZE_M):

    if obj['y'] > 0 and obj['x'] > 0:
        obj['x'] -= 1
        obj['y'] -= 1
        

    

moves = {
    'w': move_up,
    's': move_down,
    'a': move_left,
    'd': move_right,
    'wa': move_up_left,
    'aw': move_up_left,
}


def get_move_handler(direction):
    return moves[direction]


while True:

    end_flag = check_state(objects)

    world_map = generate_map(objects, SIZE_N, SIZE_M)

    print(f'Turns: {turns}')
    print_map(world_map)

    if end_flag:
        break
    
    for obj in filter(lambda o: o['movable'], objects):

        direction = ''

        if obj['type'] == 'char':
            direction = input('Enter action (w / s / a / d) ')
        elif obj['type'] == 'enemy':
            direction = choice(('w', 's', 'a', 'd', 'aw'))
        
        move_handler = get_move_handler(direction)
        move_handler(obj)

    turns += 1
    save(objects, turns, SIZE_N, SIZE_M)

    print()