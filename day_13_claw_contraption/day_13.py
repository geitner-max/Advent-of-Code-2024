
__author__ = "Maximilian Geitner"
__date__ = "13.12.2024"

# idea: naive solution
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

    prize_x = int(parts_prize[0].replace("X=", ""))
    prize_y = int(parts_prize[1].replace("Y=", ""))
    # find configuration with minimal token costs
    minimum_token_cost = None

    for i in range(100, 0, -1):
        remaining_x = prize_x - x_b * i
        remaining_y = prize_y - y_b * i

        for j in range(0, 101):
            remaining_x2 = remaining_x - (x_a * j)
            remaining_y2 = remaining_y - (y_a * j)
            if remaining_x2 == 0 and remaining_y2 == 0:
                token_cost =  i + 3 * j
                if minimum_token_cost is None or token_cost < minimum_token_cost:
                    minimum_token_cost = token_cost

    if minimum_token_cost is None:
        return 0
    else:
        return minimum_token_cost



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
    # process last scenario additionally
    value = evaluate_scenario(scenario)
    scenario = []
    result += value

    # 3.) output solution
    print("Solution Day 13 Part 1: ", result)
