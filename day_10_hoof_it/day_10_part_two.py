
__author__ = "Maximilian Geitner"
__date__ = "10.12.2024"

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def move_to_next_position(cur_x, cur_y, direction):
    diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return cur_x + diff[direction][0], cur_y + diff[direction][1]

def is_in_bounds(cur_x, cur_y, cols, rows):
    return 0 <= cur_x < cols and 0 <= cur_y < rows

# change from part one to part two: do not check visited field and keep all possible paths active
def visit_trailheads(level_map, start_x, start_y, cols, rows):
    visited = []
    for i in range(rows):
        visited.append([False] * cols)
    queue = [(start_x, start_y)]
    result_trailhead = 0
    while len(queue) > 0:
        next_list = []
        for x, y in queue:
            for i in range(4):
                next_x, next_y = move_to_next_position(x, y, i)
                if is_in_bounds(next_x, next_y, cols, rows):
                    if level_map[next_y][next_x] == level_map[y][x] + 1:
                        next_list.append((next_x, next_y))
                        if level_map[next_y][next_x] == 9:
                            result_trailhead += 1
        queue = next_list
    return result_trailhead

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    level = []
    level_columns = 0
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            parts_int = list(map(lambda x: int(x), list(line)))
            level_columns = len(parts_int)
            level.append(parts_int)

    level_rows = len(level)
    result = 0
    # 2.) perform modified path finding algorithm
    for j in range(level_rows):
        for i in range(level_columns):
            if level[j][i] == 0:
                result += visit_trailheads(level, i, j, level_columns, level_rows)
    # 3.) print result
    print("Solution Day 10 Part 1: ", result)
