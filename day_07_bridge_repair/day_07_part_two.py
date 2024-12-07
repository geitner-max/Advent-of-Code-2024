
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
                found_sol = False
                # 2.) try all  3^(n - 1) combinations of multiplication, plus and concat operation
                for i in range(pow(3, len(input_values) - 1)):
                    value = input_values[0]
                    # add product or plus
                    for j in range(1, len(input_values)):
                        div = pow(3, j - 1)
                        to_compare = (i // div) % 3

                        if to_compare == 0:
                            # product
                            value *= input_values[j]
                        elif to_compare == 1:
                            # plus
                            value += input_values[j]
                        else:
                            # concat
                            value = int(str(value) + str(input_values[j]))

                        if value > desired_outcome:
                            break

                    # evaluate result
                    if desired_outcome == value:
                        total += 1
                        found_sol = True
                    if found_sol:
                        break

            if total > 0:
                result += desired_outcome

        # 3.) output result
        # runtime: 1 minute
        print("Solution Day 7 Part 2: ", result)
