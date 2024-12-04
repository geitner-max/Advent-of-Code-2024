
__author__ = "Maximilian Geitner"
__date__ = "04.12.2024"

def get_char(col_index, row_index, arr):
    return arr[row_index][col_index]

def get_patterns():
    # row per row
    to_find_1 = [['M', 'X', 'S'], ['X', 'A', 'X'], ['M', 'X', 'S']]
    to_find_2 = [['M', 'X', 'M'], ['X', 'A', 'X'], ['S', 'X', 'S']]
    to_find_3 = [['S', 'X', 'S'], ['X', 'A', 'X'], ['M', 'X', 'M']]
    to_find_4 = [['S', 'X', 'M'], ['X', 'A', 'X'], ['S', 'X', 'M']]
    return [to_find_1, to_find_2, to_find_3, to_find_4]

def find_xmas(start_x, start_y,  arr, columns, rows):
    end_pos_x = start_x + 2
    end_pos_y = start_y + 2
    if 0 <= end_pos_x < columns and 0 <= end_pos_y < rows:
        for pattern in get_patterns():
            count = 0
            for index_y in range(3):
                for index_x, c in enumerate(pattern[index_y]):
                    if get_char(start_x + index_x, start_y + index_y, arr) == c or c == 'X':
                        count += 1
                    else:
                        break
            if count == 9:

                return 1

        return 0
    else:
        return 0

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example_part_two.txt"

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

    # 2.) starting at given position, try to match one of four 3 x 3 pattern
    total = 0
    for i in range(rows_total):
        for j in range(cols_total):
            total += find_xmas(j, i, arr_chars, cols_total, rows_total)

    print("Solution Day 4 Part 2: ", total)