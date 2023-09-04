

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


def save(objects, turns, size_n, size_m):
    # 14 14 X char
    with open('save.txt', 'w') as file:

        file.write(f'{size_n} {size_m}\n')
        file.write(f'{turns}\n')

        for obj in objects:
            file.write(f"{obj['x']} {obj['y']} {obj['sign']} {obj['type']} \n")

    print('Game saved!')