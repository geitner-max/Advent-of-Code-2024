__author__ = "Maximilian Geitner"
__date__ = "09.12.2024"

from functools import reduce


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    # example: 2333133121414131402
    arr_parts: list = []
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            arr_parts = list(map(lambda x: int(x), list(line)))

    space_required = reduce(lambda x, y: x +y, arr_parts)

    cur_index = 0
    file_id = 0

    # 2.) split into free space and files
    temp_offset = 0
    arr_index = []  # array contains offset to free_space or file_id
    for val in arr_parts:
        arr_index.append(temp_offset)
        temp_offset += val
    # arrays containing all file_sizes from file_id 0 to (n - 1), file_sizes_start contains the offset of each file
    file_sizes = list(map(lambda item: item[1], filter(lambda item: item[0] % 2 == 0, enumerate(arr_parts))))
    file_sizes_start = list(map(lambda item: arr_index[item[0]], filter(lambda item: item[0] % 2 == 0, enumerate(arr_parts))))
    # arrays containing length of free space and offset position
    free_spaces = list(map(lambda item: item[1], filter(lambda item: item[0] % 2 == 1, enumerate(arr_parts))))
    free_spaces_start = list(
        map(lambda item: arr_index[item[0]], filter(lambda item: item[0] % 2 == 1, enumerate(arr_parts))))

    # 3.) assign files to the first free spaces if possible, from right to left
    for file_id in range(len(file_sizes) - 1, 0, -1):
        file_size = file_sizes[file_id]
        copy_success = False
        for free_space_index in range(file_id):
            if free_spaces[free_space_index] >= file_size:
                # can copy
                file_sizes_start[file_id] = free_spaces_start[free_space_index]
                free_spaces_start[free_space_index] += file_size
                free_spaces[free_space_index] -= file_size
                break


    # 4.) calculate checksum and output solution
    result = 0
    for file_id in range(len(file_sizes)):
        for i in range(file_sizes[file_id]):
            result += (file_sizes_start[file_id] + i) * file_id
    print("Solution Day 9 Part 2: ", result)
