
__author__ = "Maximilian Geitner"
__date__ = "06.12.2024"

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def get_char(level_map, x, y):
    return level_map[y][x]

def is_in_level(level_map, x, y):
    return 0 <= x < len(level_map[0]) and 0 <= y < len(level[1])

def get_next_position(level_map, cur_x, cur_y, direction_move):
    while True:
        next_x, next_y = move_one_step(cur_x, cur_y, direction_move)
        if not is_in_level(level_map, next_x, next_y):
            return next_x, next_y, direction_move
        elif get_char(level_map, next_x, next_y) != '#':
            return next_x, next_y, direction_move
        else:
            direction_move = (direction_move + 1) % 4

def move_one_step(cur_x, cur_y, direction_move):
    if direction_move == UP:
        return cur_x, cur_y - 1
    elif direction_move == RIGHT:
        return cur_x + 1, cur_y
    elif direction_move == DOWN:
        return cur_x, cur_y + 1
    else:
        return cur_x - 1, cur_y

def set_visited(arr_visited, x, y):
    arr_visited[y][x] = True

def set_visited_set(arr_visited, x, y, dir_move):
    arr_visited.add ((x, y, dir_move))

def is_visited_set(arr_visited: set, x, y, dir_move):
    return (x, y, dir_move) in arr_visited

def check_scenario(level_map, initial_x, initial_y, obstruction_x, obstruction_y):
    if get_char(level_map, obstruction_x, obstruction_y) != '.':
        return False
    else:
        # add obstruction
        level_map[obstruction_y][obstruction_x] = '#'
    # replay level
    # return True if guard meet visited field
    # return Fals if guard leaves map
    arr_visited = set()
    arr_visited.add((initial_x, initial_y, UP))
    pos_x = initial_x
    pos_y = initial_y
    direction = UP
    while True:
        pos_x, pos_y, direction = get_next_position(level_map, pos_x, pos_y, direction)
        # print(pos_x, pos_y)
        if not is_in_level(level, pos_x, pos_y):
            level_map[obstruction_y][obstruction_x] = '.'
            return False
        if is_visited_set(arr_visited, pos_x, pos_y, direction):
            level_map[obstruction_y][obstruction_x] = '.'
            return True
        set_visited_set(arr_visited, pos_x, pos_y, direction)


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input

    direction_1 = UP

    level = []
    visited: list = []
    position_x = 0
    position_y = 0
    start_x = 0
    start_y = 0
    with open(filename) as file:
        row_index = 0
        for line in file:
            line: str = line.replace("\n", "")
            level.append(list(line))
            visited.append([False] * len(line))
            if '^' in line:
                position_x = line.index('^')
                position_y = row_index
                start_x = position_x
                start_y = position_y
                set_visited(visited, position_x, position_y)

            row_index += 1

    # 2.) Solve Part one: Simulate guard movements until guard leaves level (is out of bounds)
    result_part_one = 0
    while True:
        position_x, position_y, direction_1 = get_next_position(level, position_x, position_y, direction_1)

        # print(pos_x, pos_y)
        if not is_in_level(level, position_x, position_y):
            break
        set_visited(visited, position_x, position_y)

    # 3.) Solution part one = Amount of visited tiles
    for row in visited:
        result_part_one += len(list(filter(lambda x: x, row)))

    print("Solution Day 6 Part 1: ", result_part_one)

    # Start Part Two
    # 4.) try to add obstruction on all previously visited positions and check for infinite loop
    #       case infinite loop: Guard visits same tile with same direction again
    #       case non-infinite loop: Guard leaves map
    result_part_two = 0
    for o_y in range(len(level)):
        for o_x in range(len(level[o_y])):
            if visited[o_y][o_x]:
                result_part_two += (1 if check_scenario(level, start_x, start_y, o_x, o_y) else 0)

    print("Solution Day 6 Part 2: ", result_part_two)
