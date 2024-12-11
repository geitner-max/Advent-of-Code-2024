
__author__ = "Maximilian Geitner"
__date__ = "11.12.2024"

def simulate_blink(number):
    if number == 0:
        return [1]
    else:
        str_num = str(number)
        if len(str_num) % 2 == 0:
            # even number of digits
            first_num = int(str_num[0: len(str_num) // 2])
            second_num = int(str_num[len(str_num) // 2:])
            return [first_num, second_num]
        else:
            return [number * 2024]

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    stones = []
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            stones = list(map(lambda x: int(x), line.split(' ')))

    # 2.) Simulate 25 steps with naive solution
    for i in range(25):
        stones_next = []
        for stone in stones:
            stones_next += simulate_blink(stone)
        stones = stones_next

    solution = len(stones)
    print("Solution Day 11 Part 1: ", solution)
