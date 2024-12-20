
__author__ = "Maximilian Geitner"
__date__ = "20.12.2024"

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def get_rows(level_map):
    return len(level_map)

def get_cols(level_map):
    return len(level_map[0])

def is_in_bounds(cur_x, cur_y, level_map):
    return 0 <= cur_x < get_cols(level_map) and 0 <= cur_y < get_rows(level_map)

def get_tile(cur_x, cur_y, level):
    return level[cur_y][cur_x]

def set_tile(cur_x, cur_y, level, value):
    level[cur_y][cur_x] = value

def map_direction_to_diff(direction):
    diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return diff[direction]

def is_visited(arr_visited, cur_x, cur_y):
    return arr_visited[cur_y][cur_x]

def set_visited(arr_visited, cur_x, cur_y, value):
    arr_visited[cur_y][cur_x] = value

def print_level(level_map):
    for row_values in level_map:
        output = "".join(row_values)
        print(output)


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    level= []
    start_x, start_y = 0, 0
    dest_x, dest_y = 0, 0
    row_index = 0
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")

            if line.find('S') != -1:
                start_x, start_y = line.find('S'), row_index
            if line.find('E') != -1:
                dest_x, dest_y = line.find('E'), row_index
            line = line.replace('S', '.').replace('E', '.')
            level.append(line)
            row_index += 1

    # 2.) perform bfs with additional cheat processing logic
    cur_list = [(start_x, start_y)]
    steps = 0
    rows = row_index
    columns = get_cols(level)
    visited = []
    for i in range(rows):
        visited.append([-1] * columns)

    cheat_states_active = []  # contains current cheats
    cheat_states_completed = []  # x, y, steps
    set_visited(visited, start_x, start_y, 0)

    while len(cur_list) > 0:
        solution_found = False
        next_list = []
        next_cheat_states_active = []
        steps += 1
        for x, y in cur_list:
            for i in range(4):
                next_x, next_y = x + map_direction_to_diff(i)[0], y + map_direction_to_diff(i)[1]
                if next_x == dest_x and next_y == dest_y:
                    solution_found = True
                if is_in_bounds(next_x, next_y, level) and is_visited(visited, next_x, next_y) == -1 and get_tile(next_x, next_y, level) != '#':
                    next_list.append((next_x, next_y))
                    set_visited(visited, next_x, next_y, steps)
                elif is_in_bounds(next_x, next_y, level) and is_visited(visited, next_x, next_y) == -1 and get_tile(next_x, next_y, level) == '#' and not solution_found:
                    # activate cheat
                    next_cheat_states_active.append((next_x, next_y))
        # evaluate active cheats
        for x, y in cheat_states_active:
            # find positions on non_walls that are not visited
            for i in range(4):
                next_x, next_y = x + map_direction_to_diff(i)[0], y + map_direction_to_diff(i)[1]
                if is_in_bounds(next_x, next_y, level) and is_visited(visited, next_x, next_y) == -1 and get_tile(
                    next_x, next_y, level) != '#':
                    cheat_states_completed.append((next_x, next_y, steps))
        cur_list = next_list
        cheat_states_active = next_cheat_states_active

    # 3.) evaluate cheats and calculate saved time compared to normal run
    dict_saved_time = {}
    cheat_step_above_100_count = 0
    for x,y, cheat_steps in cheat_states_completed:
        if cheat_steps < steps and is_visited(visited, x, y) > 0 and is_visited(visited, x, y) > cheat_steps:
            diff = is_visited(visited, x, y) - cheat_steps
            if diff >= 100:
                cheat_step_above_100_count += 1

            if diff in dict_saved_time:
                dict_saved_time[diff] += 1
            else:
                dict_saved_time[diff] = 1


    print("Solution Day 20 Part 1: ", cheat_step_above_100_count)
