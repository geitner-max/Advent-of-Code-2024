
__author__ = "Maximilian Geitner"
__date__ = "07.12.2024"

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    result = 0
    with open(filename) as file:

        for line in file:
            line: str = line.replace("\n", "")
            index_first_part = line.index(':')
            desired_outcome = int(line[0:index_first_part])
            remaining_values_str = line[index_first_part + 2:]

            input_values = list(map(lambda x: int(x), remaining_values_str.split(' ')))

            total = 0
            if len(input_values) == 1:
                if input_values[0] == desired_outcome:
                    total += 1
            else:
                # 2.) try all  2^(n - 1) combinations of multiplication and plus sign
                for i in range(pow(2, len(input_values) - 1)):
                    value = input_values[0]
                    # add product or plus
                    for j in range(1, len(input_values)):
                        bit_shift_val = 1 << (j - 1)
                        if (i & bit_shift_val) != 0:
                            # product
                            value *= input_values[j]
                        else:
                            # plus
                            value += input_values[j]

                    if desired_outcome == value:
                        total += 1

            if total > 0:
                result += desired_outcome
        # 3.) output result
        print("Solution Day 7 Part 1: ", result)