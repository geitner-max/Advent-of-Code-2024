import numpy as np

__author__ = "Maximilian Geitner"
__date__ = "13.12.2024"

# idea: intersection between two lines
#
def evaluate_scenario(input_scenario):
    parts_a = input_scenario[0].replace("Button A: ", "").replace(" ", "").split(",")
    parts_b = input_scenario[1].replace("Button B: ", "").replace(" ", "").split(",")
    parts_prize = input_scenario[2].replace("Prize: ", "").replace(" ", "").split(",")
    # button A
    x_a = int(parts_a[0].replace("X+", ""))
    y_a = int(parts_a[1].replace("Y+", ""))
    # button B
    x_b = int(parts_b[0].replace("X+", ""))
    y_b = int(parts_b[1].replace("Y+", ""))
    offset = 10000000000000

    prize_x = int(parts_prize[0].replace("X=", "")) + offset
    prize_y = int(parts_prize[1].replace("Y=", "")) + offset

    # create two lines defined by points A-B and C-D
    a_x, a_y = 0, (prize_x/x_b)
    b_x, b_y = x_b, (prize_x/x_b) - x_a

    c_x, c_y = 0, (prize_y/y_b)
    d_x, d_y = y_b, (prize_y/y_b) - y_a
    # find intersection point
    if is_parallel(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        # special case parallel: does not happen in example or input
        print("Error: Case Parallel")
    else:
        # case not parallel
        # px is the amount of button A presses
        # py is the amount of button B presses
        px = np.round(calculate_px(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y))
        py = np.round(calculate_py(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y))

        if px * x_a + py * x_b == prize_x and px * y_a + y_b * py == prize_y:
            # solution: cost tokens
            return int(px * 3 + py)
    return 0

def is_parallel(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
    return (b_y - a_y) * (d_x - c_x) == (b_x - a_x) * (d_y - c_y)


def calculate_px(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
    nominator = (b_x - a_x) * (c_x * d_y - d_x * c_y) - (d_x - c_x) * (a_x * b_y - b_x * a_y)
    denominator = (b_x - a_x) * (d_y - c_y) - (b_y - a_y) * (d_x - c_x)
    return nominator / denominator

def calculate_py(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
    nominator = (b_y - a_y) * (c_x * d_y - d_x * c_y) - (d_y - c_y) * (a_x * b_y - b_x * a_y)
    denominator = (b_x - a_x) * (d_y - c_y) - (b_y - a_y) * (d_x - c_x)
    return nominator / denominator



def calc_tokens(am_a, am_b):
    return am_a * 3 + am_b

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input

    scenario = []
    result = 0
    # 2.) process scenarios
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            if line != "":
                scenario.append(line)
            else:
                value = evaluate_scenario(scenario)
                scenario = []
                result += value
    # process last scenario separately
    value = evaluate_scenario(scenario)
    scenario = []
    result += value
    # 3.) print
    print("Solution Day 13 Part 2: ", result)
