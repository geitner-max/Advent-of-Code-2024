
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
        filename = "example.txt"

    # 1.) Read Input
    instructions = []
    result = 0
    with open(filename) as file:
        for line in file:
            line: str = line.replace("\n", "")

            # 2.) for each starting position, check whether format  "mul(x, y)" with x and y as sequence of digits can be extracted
            # add computed product of x and y to result if the format is present
            for i in range(len(line)):
                 result += extract_number(line, i)

    # 3.) Output solution
    print("Solution Day 3 Part 1: ", result)
