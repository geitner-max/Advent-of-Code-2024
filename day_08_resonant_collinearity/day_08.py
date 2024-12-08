
__author__ = "Maximilian Geitner"
__date__ = "08.12.2024"

def get_node(level_map, x, y):
    return level_map[y][x]

def get_distance(cur_x, cur_y, antenna_x, antenna_y):
    return [(cur_x - antenna_x), (cur_y - antenna_y)]


# idea: - get a list of distances between selected tile and antenna
#       - find matching where one entry is double the value of another entry
def is_antinode(antenna_values: list):
    for x0, y0 in antenna_values:
        for x1, y1 in antenna_values:
            if ((x0 == 2 * x1 and y0 == 2 * y1) or (2 * x0 == x1 and 2 * y0 ==  y1)) and (x0 != 0 and y0 != 0) and (x1 != 0 and y1 != 0):
                print(x0, y0, ", ", x1, y1)
                return True
    return False

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    level = []
    rows = 0
    cols = 0
    antennas = []
    with open(filename) as file:
        for line in file:
            line: str = line.replace("\n", "")
            level.append(list(line))

            cols = len(list(line))
            for index, node in enumerate(line):
                if node != '.':
                    antennas.append((node, index, rows))

            rows += 1

    # 2.) find letters and digits (antenna frequencies) in input
    antenna_groups =set(map(lambda item: item[0], antennas))

    result = 0
    # 3.) for each tile, compute distances to other antennas and find entries matching the required conditions
    #       of being in a line and double the distances
    for row_index in range(rows):
        for col_index in range(cols):
            antenna_distances = list(map(lambda item: (item[0], get_distance(cur_x=col_index, cur_y=row_index, antenna_x=item[1], antenna_y = item[2])), antennas))

            for antenna_value in antenna_groups:
                antenna_distances_same_value = list(map(lambda item: item[1], filter(lambda item: item[0] == antenna_value, antenna_distances)))

                if is_antinode(antenna_distances_same_value):
                    result += 1
                    print(row_index, col_index, antenna_value)
                    break
    # 4.) output solution
    print("Day 8 Part 1: ", result)