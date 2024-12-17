
__author__ = "Maximilian Geitner"
__date__ = "16.12.2024"

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def get_rows(level):
    return len(level)

def get_cols(level):
    return len(level[0])

def is_in_bounds(cur_x, cur_y, level):
    return 0 <= cur_x < get_cols(level) and 0 <= get_rows(level)

def get_tile(cur_x, cur_y, level):
    return level[cur_y][cur_x]


def map_direction_to_diff(direction):
    diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return diff[direction]

def get_visited(visited, cur_x, cur_y, direction):
    return visited[cur_y][cur_x][direction]

def set_visited(visited, cur_x, cur_y, direction, points):
    visited[cur_y][cur_x][direction] = points

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example_2.txt"

    # 1.) Read Input
    level = []
    s_x, s_y = 0, 0
    t_x, t_y = 0, 0
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            level.append(list(line))
            if line.find('S') != -1:
                s_x, s_y = line.find('S'), len(level) - 1
            if line.find('E') != -1:
                t_x, t_y = line.find('E'), len(level) - 1

    rows = get_rows(level)
    cols = get_cols(level)
    # 2.) init visited array
    arr_visited = []
    for j in range(rows):
        arr_row = []
        for i in range(cols):
            arr_row.append([-1] * 4)
        arr_visited.append(arr_row)


    # 3.) perform algorithm
    # idea: bfs with additional score increasing by taking steps and changing direction
    cur_list = [(s_x, s_y, RIGHT, 0)]
    set_visited(arr_visited, s_x, s_y, RIGHT, 0)

    while len(cur_list) > 0:
        next_list = []
        for x, y, direction, points in cur_list:
            # calculate next positions
            for target_dir in range(4):
                target_diff = abs((direction - target_dir + 4) % 4)
                if target_diff == 3:
                    target_diff = 1
                # check valid movement
                next_x, next_y = x + map_direction_to_diff(target_dir)[0], y + map_direction_to_diff(target_dir)[1]
                next_points = points + 1 + target_diff * 1000
                if get_tile(next_x, next_y, level) != '#' and (get_visited(arr_visited, next_x, next_y, target_dir) == -1 or next_points < get_visited(arr_visited, next_x, next_y, target_dir)):
                    next_list.append((next_x, next_y, target_dir, next_points))
                    set_visited(arr_visited, next_x, next_y, target_dir, next_points)
        cur_list = next_list

    # ------------------- START PART TWO --------------------------
    # 4.) identify direction on target tile with lowest score and output solution for part one
    min_points = None
    target_dir = 0
    for i in range(4):
        if min_points is None or get_visited(arr_visited, t_x, t_y, i) < min_points and get_visited(arr_visited, t_x, t_y, i) != -1:
            min_points = get_visited(arr_visited, t_x, t_y, i)
            target_dir = i
    print("Solution Day 16 Part 1: ", min_points)  # solution for part one

    # 5.) Perform reverse path finding based on neighbouring non-wall tiles and valid scores for best paths
    # mark best seat tiles with value = 1
    cur_list =[(t_x, t_y, target_dir, min_points)]
    best_seats = []
    for j in range(rows):
        best_seats.append([0] * cols)

    while len(cur_list) > 0:
        next_list = []
        for x, y, cur_dir, points in cur_list:
            best_seats[y][x] = 1

            for dir_from_cur_pos in range(4):
                opposite_dir = ((dir_from_cur_pos + 2)%4)
                next_x, next_y = x + map_direction_to_diff(dir_from_cur_pos)[0], y + map_direction_to_diff(dir_from_cur_pos)[1]

                for dir_prev_pos in range(4):

                    target_diff = abs((opposite_dir - dir_prev_pos + 4) % 4)
                    if target_diff == 3:
                        target_diff = 1
                    target_points = points - 1 - target_diff * 1000

                    prev_points = get_visited(arr_visited, next_x, next_y, dir_prev_pos)
                    if get_tile(next_x, next_y, level) != '#' and prev_points == target_points and target_points >= 0:
                        next_list.append((next_x, next_y, (dir_from_cur_pos + 2) % 4, prev_points))
        cur_list = next_list
    # 6.) count amount of best seats and output results
    result = 0
    for j in range(rows):
        for i  in range(cols):
            result += best_seats[j][i]

    print("Solution Day 16 Part 2: ", result)
