
__author__ = "Maximilian Geitner"
__date__ = "01.12.2024"

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    left_side = []
    right_side = []
    # 1.) Read Input
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split("   ")

            left_side.append(int(parts[0]))
            right_side.append(int(parts[1]))

    # 2.) Sort Both sides
    left_side.sort()
    right_side.sort()

    solution_part_one = 0
    for i in range(len(left_side)):
        diff = abs(left_side[i] - right_side[i])
        solution_part_one += diff

    print("Solution Pat One: ", solution_part_one)

    # Part Two
    # 1.) Find all unique values on the left side
    values = set(left_side)

    similarity_score = 0
    # 2.) For each value, sum up the product of occurences of the number on both sides
    for value in values:
        occurences_left = len(list(filter(lambda x: x == value, left_side)))
        occurences_right = len(list(filter(lambda x: x == value, right_side)))
        score = value * occurences_left * occurences_right
        similarity_score += score
    print("Solution Part Two: ", similarity_score)
