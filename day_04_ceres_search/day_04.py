
__author__ = "Maximilian Geitner"
__date__ = "04.12.2024"

def get_char(col_index, row_index, arr):
    return arr[row_index][col_index]


def find_xmas(start_x, start_y, dir_x, dir_y, arr, columns, rows):
    end_pos_x = start_x + 3 * dir_x
    end_pos_y = start_y + 3 * dir_y
    if 0 <= end_pos_x < columns and 0 <= end_pos_y < rows:
        to_find = ['X', 'M', 'A', 'S']
        for index, c in enumerate(to_find):
            if get_char(start_x + index * dir_x, start_y + index * dir_y, arr) != to_find[index]:
                return 0
        return 1
    else:
        return 0

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    lines = []
    arr_chars = []
    cols_total = 1
    rows_total = 1
    with open(filename) as file:
        for line in file:
            line: str = line.replace("\n", "")
            lines.append(line)

            cols_total = len(line)
            chars = []
            for c in line:
                chars.append(c)
            arr_chars.append(chars)
    rows_total = len(lines)

    # try all combinations for xmas starting at this tile
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    total = 0
    for i in range(rows_total):
        for j in range(cols_total):
            for (x, y) in dirs:
                total += find_xmas(j, i, x, y, arr_chars, cols_total, rows_total)

    print("Solution Day 4 Part 1: ", total)