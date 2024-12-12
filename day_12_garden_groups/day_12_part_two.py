
__author__ = "Maximilian Geitner"
__date__ = "12.12.2024"

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def calc_perimeter(level_map, arr_visited, x_input, y_input, column_count, row_count):
    diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    region_count_res = 1
    cur_list = [(x_input, y_input)]
    set_visited(x_input, y_input, arr_visited)
    # change: save perimeter as position (x, y, direction)
    fence_row: set = set()
    fence_col: set = set()

    while len(cur_list) > 0:
        next_list = []
        for x, y in cur_list:
            for m in range(4):
                diff_x, diff_y = diff[m]
                pos_x = x + diff_x
                pos_y = y + diff_y
                # perimeter check
                if is_in_bounds(pos_x, pos_y, column_count, row_count):
                    # add fences
                    if level_map[y][x] != level_map[pos_y][pos_x]:
                        if m == 0:
                            fence_row.add((x, y + 1, DOWN))
                        elif m == 1:
                            fence_row.add((x, y, UP))
                        elif m == 2:
                            fence_col.add((x + 1, y, RIGHT))
                        else:
                            fence_col.add((x, y, LEFT))
                    elif level_map[y][x] == level_map[pos_y][pos_x] and not is_visited(pos_x, pos_y, arr_visited):
                        next_list.append((pos_x, pos_y))
                        set_visited(pos_x, pos_y, arr_visited)
                        region_count_res += 1
                else:
                    if m == 0:
                        fence_row.add((x, y + 1, DOWN))
                    elif m == 1:
                        fence_row.add((x, y, UP))
                    elif m == 2:
                        fence_col.add((x + 1, y, RIGHT))
                    else:
                        fence_col.add((x, y, LEFT))
        cur_list = next_list
    region_peri = len(fence_row) + len(fence_col)
    # count required sides
    region_peri = count_sides_column(fence_col) + count_sides_row(fence_row)

    return region_peri, region_count_res

def count_sides_row(perimeters):
    visited_set = set()
    diff = [(1, 0), (-1, 0)]
    result_peri = 0
    for start_x, start_y, side in perimeters:
        if (start_x, start_y) not in visited_set:
            result_peri += 1
            cur_list = [(start_x, start_y)]
            visited_set.add((start_x, start_y))
            while len(cur_list) > 0:
                next_list = []
                for x, y in cur_list:
                    for m in range(2):
                        diff_x, diff_y = diff[m]
                        pos_x = x + diff_x
                        pos_y = y + diff_y
                        if (pos_x, pos_y, side) in perimeters and (pos_x, pos_y) not in visited_set:
                            next_list.append((pos_x, pos_y))
                            visited_set.add((pos_x, pos_y))
                cur_list = next_list
    return result_peri

def count_sides_column(perimeters):
    visited_set = set()

    diff = [(0, 1), (0, -1)]

    result_peri = 0
    for start_x, start_y, side in perimeters:
        if (start_x, start_y) not in visited_set:
            result_peri += 1
            cur_list = [(start_x, start_y)]
            visited_set.add((start_x, start_y))
            while len(cur_list) > 0:
                next_list = []
                for x, y in cur_list:
                    for m in range(2):
                        diff_x, diff_y = diff[m]
                        pos_x = x + diff_x
                        pos_y = y + diff_y
                        if (pos_x, pos_y, side) in perimeters and (pos_x, pos_y) not in visited_set:
                            next_list.append((pos_x, pos_y))
                            visited_set.add((pos_x, pos_y))
                cur_list = next_list
    return result_peri

def is_in_bounds(x, y, column_count, row_count):
    return 0 <= x < column_count and 0 <= y < row_count


def is_visited(x, y, arr_visited):
    return arr_visited[y][x]


def set_visited(x, y, arr_visited):
    arr_visited[y][x] = True


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example_2.txt"

    # 1.) Read Input
    level = []
    region_values = set()
    cols = 0
    rows = 0
    visited = []
    with open(filename) as file:

        for line in file:
            rows += 1
            line: str = line.replace("\n", "")
            cols = len(line)
            level.append(list(line))
            visited.append([False] * cols)
            for val in line:
                region_values.add(val)

    # 2.) apply modified algorithm
    result = 0
    for j in range(rows):
        for i in range(cols):
            if not is_visited(i, j, visited):
                region_val = level[j][i]
                peri, count = calc_perimeter(level, visited, i, j, cols, rows)
                result += peri * count

    print("Solution Day 12 Part 2: ", result)
