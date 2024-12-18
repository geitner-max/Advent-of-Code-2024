
__author__ = "Maximilian Geitner"
__date__ = "18.12.2024"

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def get_rows(level):
    return len(level)

def get_cols(level):
    return len(level[0])

def is_in_bounds(cur_x, cur_y, level):
    return 0 <= cur_x < get_cols(level) and 0 <= cur_y < get_rows(level)

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
    rows = 71
    columns = 71
    max_bytes_fallen = 1024

    if use_example:
        filename = "example.txt"
        rows = 7
        columns = 7
        max_bytes_fallen = 12
    # 1.) Read Input

    level = []
    visited = []

    for j in range(rows):
        level.append(['.'] * columns)
        visited.append([False] * columns)

    bytes_fallen = 0
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            parts = line.split(",")
            set_tile(int(parts[0]), int(parts[1]), level, '#')
            # only consider 1024 items
            bytes_fallen += 1
            if bytes_fallen == max_bytes_fallen:
                break

    cur_list = [(0, 0)]
    steps = 0
    # apply bfs to the map with first 1024 fallen bytes
    while len(cur_list) > 0:
        solution_found = False
        next_list = []
        steps += 1
        for x, y in cur_list:
            for i in range(4):
                next_x, next_y = x + map_direction_to_diff(i)[0], y + map_direction_to_diff(i)[1]
                if next_x == rows - 1 and next_y == columns - 1:
                    print("Solution Day 18 Part 1: ", steps)
                    solution_found = True
                    break
                if is_in_bounds(next_x, next_y, level) and not is_visited(visited, next_x, next_y) and get_tile(next_x, next_y, level) != '#':
                    next_list.append((next_x, next_y))
                    set_visited(visited, next_x, next_y, True)
        if solution_found:
            break
        cur_list = next_list
