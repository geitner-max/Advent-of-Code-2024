
__author__ = "Maximilian Geitner"
__date__ = "05.12.2024"

def check_update(mapping_rules, row_values: list, mappingOrder):
    incorrect_mappings = []
    for (x, y) in mapping_rules:
        first_value_found = False
        second_value_found = False
        for val in row_values:
            if val == x:
                first_value_found = True
                if second_value_found:
                    incorrect_mappings.append((x, y))
                    break
            if val == y:
                second_value_found = True
    # only count incorrect update mappings
    if len(incorrect_mappings) > 0:
        row_values = reorder_mapping(row_values, incorrect_mappings, mappingOrder)
        middle_index = len(row_values) // 2
        return row_values[middle_index]
    else:
        return 0

def is_in_valid_position(val, set_remaining: set, mappingOrder):
    if val in mappingOrder:
        set_predecssors = mappingOrder[val]
        set_intersection = set_remaining.intersection(set_predecssors)
        return len(set_intersection) == 0
    else:
        return True

# idea: find valid reordering by looking at remaining numbers and required predecessors for each remaining number
# number can appear in sequence if both set of remaining numbers and set of predecessors does not intersect
def reorder_mapping(row_values, incorrect_mappings, mappingOrder):
    set_incorrect = set()
    set_remaining = set(row_values)
    for (a, b) in incorrect_mappings:
        set_incorrect.add(a)
        set_incorrect.add(b)

    correct_ordering = []
    buffer = row_values

    while len(buffer) != 0:
        for valB in buffer:
            if is_in_valid_position(valB, set_remaining, mappingOrder):
                set_remaining.remove(valB)
                correct_ordering.append(valB)
                buffer.remove(valB)
                break

    return correct_ordering


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    mapping = []
    mapping_extended = {}
    phase = 0

    result = 0
    with open(filename) as file:
        for line in file:
            line: str = line.replace("\n", "")

            if phase == 0:
                if line == '':
                    phase = 1
                    # calculate extended mapping rules
                    for (x, y) in mapping:
                        if y in mapping_extended:
                            mapping_extended[y].add(x)
                        else:
                            init_set =  set()
                            init_set.add(x)
                            mapping_extended[y] = init_set

                else:
                    parts = line.split('|')
                    mapping.append((int(parts[0]), int(parts[1])))
            else:
                parts = line.split(',')
                update_row = list(map(lambda x : int(x), parts))
                result += check_update(mapping, update_row, mapping_extended)

    print("Solution Day 5 Part 2: ", result)
