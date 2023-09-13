# | | | |O| |
# | | | | | |
# | | | | | |
# | |X| | | |

from random import randint, choice

from config import Config
from entities import Enemy, Character, Portal
# from game_engine.map import generate_map, print_map
from game_map import generate_map, print_map
# from game_engine.tools import load, save
from tools import load, save


is_load = input('Do you want to load game? (y/''): ')
config = Config()

if is_load.casefold() == 'y':
    objects, turns, config.size_n, config.size_m = load()
else:

    char = Character(randint(0, config.size_n - 1), randint(0, config.size_m - 1))
    portal = Portal(randint(0, config.size_n - 1), randint(0, config.size_m - 1))
    enemies = [Enemy(randint(0, config.size_n - 1), randint(0, config.size_m - 1)) for _ in range(5)]
    objects = [char, portal] + enemies

    turns = 0


def check_state(objects):

    for obj in objects:

        if isinstance(obj, Character):
            char  = obj
        elif isinstance(obj, Portal):
            portal = obj
        elif isinstance(obj, Enemy):
            loss_condition = char.x == obj.x and \
                            char.y == obj.y
            
            if loss_condition:
                char.sign = 'L'
                print(f'You LOST in {turns} turns')
                break

    win_condition = char.x == portal.x and \
                    char.y == portal.y
    
    if win_condition:
        char.sign = 'W'
        print(f'You WON in {turns} turns')        

    return win_condition or loss_condition



while True:

    end_flag = check_state(objects)

    world_map = generate_map(objects, config.size_n, config.size_m)

    print(f'Turns: {turns}')
    print_map(world_map)

    if end_flag:
        break
    
    for obj in filter(lambda o: o.movable, objects):

        direction = ''

        if isinstance(obj, Character):
            direction = input('Enter action (w / s / a / d) ')
        elif isinstance(obj, Enemy):
            direction = choice(('w', 's', 'a', 'd', 'aw'))
        
        obj.move(direction)

    turns += 1
    save(objects, turns, config.size_n, config.size_m)

    print()