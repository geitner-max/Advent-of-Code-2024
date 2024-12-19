
__author__ = "Maximilian Geitner"
__date__ = "19.12.2024"

def solve_rec(desired_design, available_designs, current_progress):
    for towel in available_designs:
        next_progress = current_progress + towel
        if desired_design == next_progress:
            return 1
        elif desired_design.startswith(next_progress):
            result = solve_rec(desired_design, available_designs, next_progress)
            if result == 1:
                return 1
            else:
                continue
    return 0

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    input_available_designs = []
    input_desired_desgins = []
    phase = 0
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            if phase == 0:
                input_available_designs = line.split(", ")
                phase = 1
            elif line != "":
                input_desired_desgins.append(line)
    solution = 0
    # 2.) filter available_designs
    # idea: filter out towels, which can be represented with other (smaller) towers in order to reduce program runtime
    unique_available_design = []
    sorted_list: list = list(sorted(input_available_designs, key=len))
    for design in sorted_list:
        if solve_rec(design, unique_available_design, "") == 0:
            unique_available_design.append(design)

    # 3.) apply brute-force algorithm for decision-making whether
    for input_desired_design in input_desired_desgins:
        solution += solve_rec(input_desired_design, unique_available_design, "")
    # 4.) output solution
    print("Solution Day 19 Part 1: ", solution)
