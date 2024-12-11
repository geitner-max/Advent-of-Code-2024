
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
    stones = {}
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            stones_list = list(map(lambda x: int(x), line.split(' ')))
            for stone in stones_list:
                stones[stone] = 1

    # 2.) Simulate 75 steps with optimized stone representation
    # idea: store a dictionary with stone_number as key and count as value
    for i in range(75):
        stones_next = {}
        for stone in stones.keys():
            # calculate stones after one step
            stone_count = stones[stone]
            stones_next_list = simulate_blink(stone)
            # add for each resulting number the current count to the next dictionary entry
            for stone_next in stones_next_list:
                if stone_next in stones_next:
                    stones_next[stone_next] += stone_count
                else:
                    stones_next[stone_next] = stone_count
        stones = stones_next

    solution = 0
    for stone_value in stones.values():
        solution += stone_value


    print("Solution Day 11 Part 2: ", solution)
