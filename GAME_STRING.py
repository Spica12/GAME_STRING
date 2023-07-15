# | | | |O| |
# | | | | | |
# | | | | | |
# | |X| | | |

from random import randint, choice

SIZE_N = randint(5, 20) # row
SIZE_M = randint(5, 20) # column


def check_state(char_x, char_y, char_sign,
                enemy_x, enemy_y,
                exit_x, exit_y):

    win_condition = char_x == exit_x and char_y == exit_y
    loss_condition = char_x == enemy_x and char_y == enemy_y

    if win_condition:
        char_sign = 'W'
        print(f'You WON in {turns} turns')
    elif loss_condition:
        char_sign = 'L'
        print(f'You LOST in {turns} turns')

    return char_sign, win_condition or loss_condition


def generate_map(char_x, char_y, char_sign,
                 enemy_x, enemy_y, enemy_sign,
                 exit_x, exit_y, exit_sign,
                 size_m=SIZE_M, size_n=SIZE_N):
    
    world_map = ''

    for j in range(size_m):
        row = '|'

        for i in range(size_n):

            if char_x == i and char_y == j:
                row += f'{char_sign}|'
            elif enemy_x == i and enemy_y == j:
                row += f'{enemy_sign}|'
            elif exit_x == i and exit_y == j:
                row += f'{exit_sign}|'
            else:
                row += ' |'
    
        world_map += f'{row}\n'

    return world_map


def move(direction, x, y, size_m=SIZE_M, size_n=SIZE_N):
    
    if direction == 'w' and y > 0:
        y -= 1
    elif direction == 's' and y < size_m - 1:
        y += 1
    elif direction == 'a' and x > 0:
        x -= 1
    elif direction == 'd' and x < size_n - 1:
        x += 1

    return x, y


char_x = 3
char_y = 2
char_sign = 'X'

enemy_x = randint(0, SIZE_N - 1)
enemy_y = randint(0, SIZE_M - 1)
enemy_sign = 'E'


exit_x = randint(0, SIZE_N - 1)
exit_y = randint(0, SIZE_M - 1)
exit_sign = 'O'

turns = 0

while True:


    char_sign, end_flag = check_state(char_x, char_y, char_sign,
                            enemy_x, enemy_y,
                            exit_x, exit_y)

    world_map = generate_map(char_x, char_y, char_sign,
                             enemy_x, enemy_y, enemy_sign, 
                             exit_x, exit_y, exit_sign)

    print(f'Turns: {turns}')
    print(world_map)

    if end_flag:
        break


    direction = input('Enter direction (w / s / a / d) ')
    char_x, char_y = move(direction, char_x, char_y)

    enemy_direction = choice('wsad')
    enemy_x, enemy_y = move(enemy_direction, enemy_x, enemy_y)

    turns += 1
    
    print()