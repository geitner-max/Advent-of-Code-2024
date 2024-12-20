
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

def get_steps_required(s_x, s_y, d_x, d_y):
    return abs(s_x - d_x) + abs(s_y - d_y)


# idea: find non-wall tiles within a distance of 20 steps and save cheat in a list for later evaluation
def apply_cheat(cur_x, cur_y, current_steps, cheats_completed, level_map):
    for next_y in range(max(0, cur_y - 21), min(cur_y + 21, get_rows(level_map))):
        for next_x in range(max(0, cur_x - 21), min(cur_x + 21, get_cols(level_map))):
            steps_required = get_steps_required(cur_x, cur_y, next_x, next_y)
            if  2 <= steps_required <= 20 and get_tile(next_x, next_y, level_map) != '#':
                cheats_completed.append((next_x, next_y, current_steps + steps_required))

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

    # 2.) bfs with modified cheat processing logic compared to part one
    cur_list = [(start_x, start_y)]
    steps = 0
    rows = row_index
    columns = get_cols(level)
    visited = []
    for i in range(rows):
        visited.append([-1] * columns)

    cheat_states_completed = []  # x, y, steps
    set_visited(visited, start_x, start_y, 0)

    activations = 0
    while len(cur_list) > 0:
        solution_found = False
        next_list = []

        for x, y in cur_list:
            if not solution_found:
                activations += 1
                apply_cheat(x, y, steps, cheat_states_completed, level)
            for i in range(4):
                next_x, next_y = x + map_direction_to_diff(i)[0], y + map_direction_to_diff(i)[1]
                if next_x == dest_x and next_y == dest_y:
                    solution_found = True
                    #break
                if is_in_bounds(next_x, next_y, level) and is_visited(visited, next_x, next_y) == -1 and get_tile(next_x, next_y, level) != '#':
                    next_list.append((next_x, next_y))
                    set_visited(visited, next_x, next_y, steps + 1)
                    # activate cheat
        # evaluate active cheats
        cur_list = next_list
        steps += 1
    # 3.) Perform evaluation similar to part one
    dict_saved_time = {}
    cheat_step_above_100_count = 0
    solution_steps = is_visited(visited, dest_x, dest_y)
    for x,y, cheat_steps in cheat_states_completed:
        if cheat_steps < is_visited(visited, dest_x, dest_y) and is_visited(visited, x, y) > cheat_steps:
            diff = is_visited(visited, x, y) - cheat_steps
            if diff >= 100:
                cheat_step_above_100_count += 1

            if diff in dict_saved_time:
                dict_saved_time[diff] += 1
            else:
                dict_saved_time[diff] = 1

    # 4.) output solution
    print("Solution Day 20 Part 2: ", cheat_step_above_100_count)
