
__author__ = "Maximilian Geitner"
__date__ = "19.12.2024"

# algorithm from part one without cache
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

# brute-force algorithm utilizing cache
def solve_rec_count(desired_design, unique_towels, cache_sol: dict, current_progress: int):
    remaining = desired_design[current_progress:]
    if remaining in cache_sol.keys():
        return cache_sol[remaining]  # if result is known
    else:
        solutions = 0
        for known_design in unique_towels:
            next_design_index = len(known_design) + current_progress
            if next_design_index < len(desired_design):
                if remaining.startswith(known_design):
                    result = solve_rec_count(desired_design, unique_towels, cache_sol, next_design_index)
                    if result > 0:
                        solutions += result
                    else:
                        continue
        # add new val to cache
        if remaining not in cache_sol:
            cache_sol[remaining] = solutions
        return solutions

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
    sorted_list: list = list(sorted(input_available_designs, key=len))
    cache_solutions = {}  # idea: cache computed solutions for character sequences and the amount of found solutions
    # 2.) perform pre-filling cache
    # if towel cannot be represented with smaller towels, assign value 1 in cache
    # otherwise assign amount of existing solutions plus one
    for design in sorted_list:
        if solve_rec(design, cache_solutions.keys(), "") == 0:
            cache_solutions[design] = 1
        else:
            res = solve_rec_count(design, input_available_designs, cache_solutions, 0)
            cache_solutions[design] = res + 1

    # 3.) run brute-force algorithm with cache, that is expanded while running the brute-algorithm
    for input_desired_design in input_desired_desgins:
        desired_design_comb = solve_rec_count(input_desired_design, input_available_designs, cache_solutions, 0)
        solution += desired_design_comb

    # 4.) output solution
    print("Day 19 Part 2: ", solution)
