
__author__ = "Maximilian Geitner"
__date__ = "14.12.2024"

def simulate_step(robots, width, height):
    robots_next = []
    for x, y, vel_x, vel_y in robots:
        next_x = (x  + vel_x + width) % width
        next_y = (y + vel_y + height) % height
        robots_next.append([next_x, next_y, vel_x, vel_y])
    return robots_next

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    width = 101
    height = 103
    input_robots = []
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")

            line = line.replace("p=", "").replace(" v=", ",")
            parts = list(map(lambda x: int(x), line.split(",")))
            input_robots.append(parts)

    # 2.) simulate until christmas pattern is found
    steps = 0
    while True:
        steps += 1
        input_robots = simulate_step(input_robots, width, height)

        # print tiles layout
        tiles = []
        for j in range(height):
            tiles.append([0] * width)

        for x, y, _, _ in input_robots:
            tiles[y][x] += 1

        # condition print current state if 20 robots are placed in a row
        print_tiles = False
        for j in range(height):
            robots_in_row = 0
            for i in range(width):
                if tiles[j][i] > 0:
                    robots_in_row += 1
                else:
                    robots_in_row = 0
                if robots_in_row > 20:
                    print_tiles = True
        if print_tiles:
            for j in range(height):
                line = ""
                for i in range(width):
                    if tiles[j][i] > 0:
                        line += "X"
                    else:
                        line += "."
                print(line)
            print("Solution Day 14 Part 2: ", steps)
            break
