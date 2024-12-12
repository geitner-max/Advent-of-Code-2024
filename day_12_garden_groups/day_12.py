
__author__ = "Maximilian Geitner"
__date__ = "12.12.2024"

def calc_perimeter(level_map, arr_visited, x_input, y_input, column_count, row_count):
    print(arr_visited)
    diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    region_count_res = 1
    region_peri = 0
    cur_list = [(x_input, y_input)]
    set_visited(x_input, y_input, arr_visited)
    while len(cur_list) > 0:
        next_list = []
        for x, y in cur_list:
            for m in range(4):
                diff_x, diff_y = diff[m]
                pos_x = x + diff_x
                pos_y = y + diff_y
                # perimeter check
                if is_in_bounds(pos_x, pos_y, column_count, row_count):
                    if level_map[y][x] != level_map[pos_y][pos_x]:
                        region_peri += 1
                    elif level_map[y][x] == level_map[pos_y][pos_x] and not is_visited(pos_x, pos_y, arr_visited):
                        next_list.append((pos_x, pos_y))
                        set_visited(pos_x, pos_y, arr_visited)
                        region_count_res += 1
                else:
                    region_peri += 1
        cur_list = next_list
    print(region_peri, region_count_res)
    return region_peri, region_count_res

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

    region_count = {}
    region_perimeter = {}
    for val in region_values:
        region_count[val] = 0
        region_perimeter[val] = 0

    result = 0
    for j in range(rows):
        for i in range(cols):
            if not is_visited(i, j, visited):
                region_val = level[j][i]
                peri, count = calc_perimeter(level, visited, i, j, cols, rows)
                result += peri * count


    print("Solution Day 12 Part 1: ", result)
