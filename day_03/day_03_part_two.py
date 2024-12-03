
__author__ = "Maximilian Geitner"
__date__ = "03.12.2024"

def extract_number(sequence, start_pos: int):
    # a) check starting string
    if start_pos + 4 < len(sequence) and sequence[start_pos: start_pos + 4] == "mul(":
        phase = 0
        num_1 = ""
        num_2 = ""
        # b) try to find x and y
        for index in range(start_pos + 4, len(sequence)):
            if phase == 0 and '0' <= sequence[index] <= '9':
                num_1 += sequence[index]
            elif phase == 0 and sequence[index] == ",":
                phase = 1
            elif phase == 1 and '0' <= sequence[index] <= '9':
                num_2 += sequence[index]
            elif phase == 1 and sequence[index] == ')':
                return int(num_1) * int(num_2)
            else:
                return 0
    return 0

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example_part_two.txt"

    # 1.) Read Input
    instructions = []
    result = 0
    is_enabled = True
    with open(filename) as file:
        for line in file:
            line: str = line.replace("\n", "")

            for i in range(len(line)):
                # 2.) add products to result similar to part one
                # extension: check for "don't()" and "do()" in order to toggle counting mechanism
                if is_enabled:
                    result += extract_number(line, i)

                if i + 7 <= len(line) and line[i: i + 7] == "don't()":
                    is_enabled = False
                if i + 4 <= len(line) and line[i: i + 4] == "do()":
                    is_enabled = True

    # 3.) Output solution
    print("Solution Day 3 Part 2: ", result)