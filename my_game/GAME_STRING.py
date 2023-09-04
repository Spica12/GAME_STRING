# | | | |O| |
# | | | | | |
# | | | | | |
# | |X| | | |

from random import randint, choice

# from game_engine.map import generate_map, print_map
from map import generate_map, print_map
from game_engine.tools import load, save





is_load = input('Do you want to load game? (y/''): ')

if is_load:
    objects, turns, SIZE_N, SIZE_M = load()
else:
    # SIZE_N = 30 # randint(10, 20) # column
    SIZE_N = randint(5, 10) # column

    # SIZE_M = 13 # randint(10, 20) # row
    SIZE_M = randint(5, 10) # row


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


def generate_enemies(count):

    enemies = []

    for _ in range(count):

        enemy = {'x': randint(0, SIZE_N - 1),
            'y': randint(0, SIZE_M - 1),
            'sign': 'E',
            'type': 'enemy'}
        
        enemies. append(enemy)

    return enemies




def move(direction, obj, size_m=SIZE_M, size_n=SIZE_N):
    
    if direction == 'w' and obj['y'] > 0:
        obj['y'] -= 1
    elif direction == 's' and obj['y'] < size_m - 1:
        obj['y'] += 1
    elif direction == 'a' and obj['x'] > 0:
        obj['x'] -= 1
    elif direction == 'd' and obj['x'] < size_n - 1:
        obj['x']+= 1









if not is_load:

    char = {'x': randint(0, SIZE_N - 1),
        'y': randint(0, SIZE_M - 1),
        'sign': 'X',
        'type': 'char'}


    portal = {'x': randint(0, SIZE_N - 1),
            'y': randint(0, SIZE_M - 1),
            'sign': 'O',
            'type': 'portal'}

    enemies = (5)

    objects = [char, portal] + enemies

    turns = 0


while True:

    end_flag = check_state(objects)

    world_map = generate_map(objects, SIZE_M, SIZE_N)

    print(f'Turns: {turns}')
    print_map(world_map)

    if end_flag:
        break
    
    for obj in objects:

        direction = ''

        if obj['type'] == 'char':
            direction = input('Enter action (w / s / a / d) ')
        elif obj['type'] == 'enemy':
            direction = choice('wsad')
        
        move(direction, obj)

    turns += 1
    save(objects, turns, SIZE_M, SIZE_N)

    print()