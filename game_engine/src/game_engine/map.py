

def generate_map(objects, size_m, size_n):
# def generate_map(objects, size_m=SIZE_M, size_n=SIZE_N):
    world_map = []

    for j in range(size_m):
        row = []

        for i in range(size_n):
            row.append(' ')

        world_map.append(row)

    for obj in objects:
        print(obj)
        world_map[obj['y']][obj['x']] = obj['sign']


    return world_map


def print_map(world_map):

    for row in world_map:
        print(f'|{"|".join(row)}|')