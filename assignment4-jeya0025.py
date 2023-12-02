def print_grid(grid):
    for row in grid:
        print(''.join(row))


def update_grid(grid, player_pos, enemy_pos):
    for row in grid:
        for i in range(len(row)):
            row[i] = '.'

    grid[player_pos['y']][player_pos['x']] = 'P'

    for enemy in enemy_pos:
        grid[enemy['y']][enemy['x']] = 'E'


def user_action(player_pos, grid_size):
    buffer_input = input("Enter a command: ").strip()
    if buffer_input.lower() == 'q':
        return False

    direction = buffer_input[0]
    steps = int(buffer_input[1:])

    if direction == 'u':
        player_pos['y'] -= steps
        if player_pos['y'] < 0:
            player_pos['y'] = 0
    elif direction == 'd':
        player_pos['y'] += steps
        if player_pos['y'] >= grid_size['y']:
            player_pos['y'] = grid_size['y'] - 1
    elif direction == 'l':
        player_pos['x'] -= steps
        if player_pos['x'] < 0:
            player_pos['x'] = 0
    elif direction == 'r':
        player_pos['x'] += steps
        if player_pos['x'] >= grid_size['x']:
            player_pos['x'] = grid_size['x'] - 1

    return True


def game_loop(grid, player_pos, enemy_pos):
    while True:
        update_grid(grid, player_pos, enemy_pos)
        print_grid(grid)
        if not user_action(player_pos, {'x': len(grid[0]), 'y': len(grid)}):
            break


# Main function
def main():
    width = 15
    height = 10

    grid = [['.' for _ in range(width)] for _ in range(height)]

    player_pos = {'x': 0, 'y': 0}

    enemy_pos = [{'x': 3, 'y': 7}, {'x': 11, 'y': 9}, {'x': 7, 'y': 4}]
    game_loop(grid, player_pos, enemy_pos)


if __name__ == "__main__":
    main()
