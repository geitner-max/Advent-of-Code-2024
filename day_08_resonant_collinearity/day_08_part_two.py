
__author__ = "Maximilian Geitner"
__date__ = "08.12.2024"

def get_node(level_map, x, y):
    return level_map[y][x]

def get_distance(cur_x, cur_y, antenna_x, antenna_y):
    return [(cur_x - antenna_x), (cur_y - antenna_y)]

def mark_anti_nodes(group, visited, col_count, row_count):
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            x, y = group[i]
            x1, y1 = group[j]
            if x != x1 or y != y1:
                # calc base distance between both antennas
                diff_x = x - x1
                diff_y = y - y1
                pos_x = x
                pos_y = y
                # mark entries going backwards
                # exit condition: leaving grid
                while True:
                    if 0 <= pos_x < col_count and 0 <= pos_y < row_count:
                        visited[pos_y][pos_x] = True
                    else:
                        break
                    pos_x = pos_x - diff_x
                    pos_y = pos_y - diff_y
                pos_x = x
                pos_y = y
                # mark entries going forward
                while True:
                    pos_x = pos_x + diff_x
                    pos_y = pos_y + diff_y
                    if 0 <= pos_x < col_count and 0 <= pos_y < row_count:
                        visited[pos_y][pos_x] = True
                    else:
                        break

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
    is_anti_node = []

    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            level.append(list(line))

            cols = len(list(line))
            is_anti_node.append([False] * cols)
            for index, node in enumerate(line):
                if node != '.':
                    antennas.append((node, index, rows))

            rows += 1


    antenna_groups =set(map(lambda item: item[0], antennas))
    result = 0
    # 2.) idea: for each pair of antennas with same frequency, compute anti_node entries
    for antenna_value in antenna_groups:
        antenna_pos_same_value = list(map(lambda item: (item[1], item[2]), filter(lambda item: item[0] == antenna_value, antennas)))
        mark_anti_nodes(antenna_pos_same_value, is_anti_node, cols, rows)

    # 3.) count marked tiles and output solution
    for row_content in is_anti_node:
        result += len(list(filter(lambda x: x, row_content)))

    print("Solution Day 8 Part 2: ", result)
