__author__ = "Maximilian Geitner"
__date__ = "09.12.2024"

from functools import reduce

def get_index(file_map, index_file, index):
    return reduce(lambda a, b: a + b, map(lambda item: item[1], filter(lambda item: item[0] < index_file, enumerate(file_map)))) + index

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    # example: 2333133121414131402
    parts = []
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            parts = list(map(lambda x: int(x), list(line)))

    # 2.) initialize file_system variable
    space_required = reduce(lambda x, y: x +y, parts)
    file_system = [-1] * space_required  # save values here, -1 is a free space, file_id otherwise
    cur_index = 0
    file_id = 0
    for index, num in enumerate(parts):
        if index % 2 == 0:
            # file
            for i in range(num):
                file_system[cur_index] = file_id
                cur_index += 1
            file_id += 1
        else:
            cur_index += num
    # 3.) Initialize pointer to first free space and last position of filesystem
    index_free_space = 1
    pointer_free_space = get_index(parts, index_free_space, 0)
    while file_system[pointer_free_space] != -1:
        index_free_space += 2
        pointer_free_space = get_index(parts, index_free_space, 0)
    pointer_to_copy = len(file_system)  - 1

    # 4.) copy values from right to left to the lowest available free space until both pointer converge at the same position

    while pointer_free_space < pointer_to_copy:
        value_file = file_system[pointer_to_copy]
        file_system[pointer_free_space] = value_file
        file_system[pointer_to_copy] = -1
        # move free space pointer
        while pointer_free_space < pointer_to_copy:
            pointer_free_space += 1
            if file_system[pointer_free_space] == -1:
                break
        # move file to copy
        while pointer_free_space < pointer_to_copy:
            pointer_to_copy -= 1
            if file_system[pointer_to_copy] != -1:
                break
        # exit condition
        if pointer_free_space >= pointer_to_copy:
            break


    # 5.) calculate checksum
    result = 0
    for i in range(len(file_system)):
        if file_system[i] == -1:
            break
        result += i * file_system[i]

    print("Solution Day 9 Part 1: ", result)