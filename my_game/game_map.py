from helpers import log_message

# Поки що не можна створити.
# Треба змінити архітектуру програми 
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
