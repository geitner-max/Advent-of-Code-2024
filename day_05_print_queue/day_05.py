
__author__ = "Maximilian Geitner"
__date__ = "05.12.2024"

def check_update(mapping_rules, row_values: list):

    for (x, y) in mapping_rules:
        first_value_found = False
        second_value_found = False
        for val in row_values:
            if val == x:
                first_value_found = True
                if second_value_found:
                    return 0 # invalid order
            if val == y:
                second_value_found = True

    middle_index = len(row_values) // 2

    return row_values[middle_index]

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    mapping = []
    phase = 0

    result = 0
    with open(filename) as file:
        for line in file:
            line: str = line.replace("\n", "")
            # 2.) read page ordering rules (phase 1) and updates (phase 2)
            if phase == 0:
                if line == '':
                    phase = 1
                else:
                    parts = line.split('|')
                    mapping.append((int(parts[0]), int(parts[1])))
            else:
                parts = line.split(',')
                update_row = list(map(lambda x : int(x), parts))
                result += check_update(mapping, update_row)

    print("Solution Day 5 Part 1: ", result)