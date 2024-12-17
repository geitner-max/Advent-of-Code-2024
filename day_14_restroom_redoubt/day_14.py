
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

    # 2.) simulate 100 steps
    for i in range(100):
        input_robots = simulate_step(input_robots, width, height)
    # 3.) evaluate quadrants
    result = 0
    tiles = [[0, 0], [0, 0]]

    for x, y, _, _ in input_robots:
        if x != width // 2 and y != height // 2:
            quadrant_x = 1 if x > width//2 else 0
            quadrant_y = 1 if y > height // 2 else 0

            tiles[quadrant_y][quadrant_x] += 1

    for j in range(2):
        tiles_with_robots = list(filter(lambda x: x != 0, tiles[j]))
        for val in tiles_with_robots:
            if result == 0:
                result = val
            else:
                result = result * val
    # 4.) output result
    print("Solution Day 14 Part 1: ", result)
