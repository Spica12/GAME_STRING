# | | | |O| |
# | | | | | |
# | | | | | |
# | |X| | | |

from random import randint, choice


def load():
    objects = []

    with open('save.txt', 'r') as file:

        for indx, line in enumerate(file):

            if indx == 0:
                map_size = line.rstrip().split()
                size_n, size_m = int(map_size[0]), int(map_size[1])
            elif indx == 1:
                turns = int(line.rstrip())
            else:
                data = line.rstrip().split()

                obj = {}
                obj['x'], obj['y'] = int(data[0]), int(data[1])
                obj['sign'] = data[2]
                obj['type'] = data[3]

                objects.append(obj)

    return objects, turns, size_n, size_m


is_load = input('Do you want to load game? (y/''): ')

if is_load:
    objects, turns, SIZE_N, SIZE_M = load()
else:
    # SIZE_N = 30 # randint(10, 20) # column
    SIZE_N = randint(10, 20) # column

    # SIZE_M = 13 # randint(10, 20) # row
    SIZE_M = randint(10, 20) # row


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


def generate_map(objects, size_m=SIZE_M, size_n=SIZE_N):
    
    world_map = []

    for j in range(size_m):
        row = []

        for i in range(size_n):
            row.append(' ')

        world_map.append(row)

    for obj in objects:
        world_map[obj['y']][obj['x']] = obj['sign']


    return world_map


def move(direction, obj, size_m=SIZE_M, size_n=SIZE_N):
    
    if direction == 'w' and obj['y'] > 0:
        obj['y'] -= 1
    elif direction == 's' and obj['y'] < size_m - 1:
        obj['y'] += 1
    elif direction == 'a' and obj['x'] > 0:
        obj['x'] -= 1
    elif direction == 'd' and obj['x'] < size_n - 1:
        obj['x']+= 1


def print_map(world_map):

    for row in world_map:
        print(f'|{"|".join(row)}|')


def save(objects, turns, size_n = SIZE_N, size_m=SIZE_M):
    # 14 14 X char
    with open('save.txt', 'w') as file:

        file.write(f'{size_n} {size_m}\n')
        file.write(f'{turns}\n')

        for obj in objects:
            file.write(f"{obj['x']} {obj['y']} {obj['sign']} {obj['type']} \n")

    print('Game saved!')



if not is_load:

    char = {'x': randint(0, SIZE_N - 1),
        'y': randint(0, SIZE_M - 1),
        'sign': 'X',
        'type': 'char'}


    portal = {'x': randint(0, SIZE_N - 1),
            'y': randint(0, SIZE_M - 1),
            'sign': 'O',
            'type': 'portal'}

    enemies = generate_enemies(10)

    objects = [char, portal] + enemies

    turns = 0


while True:

    end_flag = check_state(objects)

    world_map = generate_map(objects)

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