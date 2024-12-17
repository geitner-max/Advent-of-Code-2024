
__author__ = "Maximilian Geitner"
__date__ = "17.12.2024"

def get_combo_operand_value(arr_registers, value):
    if 0 <= value <= 3:
        return value
    elif 4 <= value <= 6:
        return arr_registers[value - 4]
    else:
        print("Error Combo Operand")
        return -1


REG_A = 0
REG_B = 1
REG_C = 2


def get_register(arr_registers, index_reg: int):
    return arr_registers[index_reg]


def set_register(arr_registers, index_reg: int, val: int):
    arr_registers[index_reg] = val

# algorithm from part one
# simulation of 3-bit computer
def get_output(reg_a, reg_b, reg_c, input_prog):
    registers = [reg_a, reg_b, reg_c]
    program = input_prog
    ip = 0
    output = []
    while ip < len(program):
        has_jumped = False
        next_instruction = program[ip]
        operand = program[ip + 1]
        if next_instruction == 0:
            # 0: adv, division, numerator in register A, denominator is 2^(combo operand)
            nom = get_register(registers, REG_A)
            denom = pow(2, get_combo_operand_value(registers, operand))
            set_register(registers, REG_A, nom // denom)
        elif next_instruction == 1:
            # 1: bxl, bitwise XOR of register B and literal operand
            result = get_register(registers, REG_B) ^ operand
            set_register(registers, REG_B, result)

        elif next_instruction == 2:
            # 2: 2: bst: value of combo operand modulo 8, write result to register B
            result = get_combo_operand_value(registers, operand) % 8
            set_register(registers, REG_B, result)

        elif next_instruction == 3:
            # jump
            if get_register(registers, REG_A) != 0:
                has_jumped = True
                lit_op = operand
                ip = lit_op
        elif next_instruction == 4:
            result = get_register(registers, REG_B) ^ get_register(registers, REG_C)
            set_register(registers, REG_B, result)

        elif next_instruction == 5:
            val = get_combo_operand_value(registers, operand) % 8
            #if len(program) < len(output) or program[len(output)] != val:
            #    return []
            output.append(val)
        elif next_instruction == 6:
            nom = get_register(registers, REG_A)
            denom = pow(2, get_combo_operand_value(registers, operand))
            set_register(registers, REG_B, nom // denom)

        elif next_instruction == 7:
            nom = get_register(registers, REG_A)
            denom = pow(2, get_combo_operand_value(registers, operand))
            set_register(registers, REG_C, nom // denom)

        if not has_jumped:
            ip += 2
    return output

# idea: backtracking
def solve_rec(complete_input, index, factor, register_val):
    # divide register space in 3-bit spaces (one for each program value)
    # start with highest value 3-bit space
    # simulate register A for each 3-bit space and find copy of program input
    for test_val in range(8):
        next_val = (factor * test_val) + register_val

        actual = get_output(next_val, 0, 0, program_input)
        index_to_read = len(complete_input) - 1 - index
        # compare position at index counting backwards in expected and actual program output
        if len(actual) == len(complete_input) and actual[index_to_read] == complete_input[index_to_read]:
            if index + 1 < len(complete_input):
                # continue with next 3-bit space
                reg_val_next = solve_rec(complete_input, index + 1, factor // 8, next_val)
                if reg_val_next is not None:
                    # recursive function has found valid solution
                    return reg_val_next
                else:
                    continue
            else:
                # solution found
                return next_val
    return None


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example_2.txt"

    # 1.) Read Input
    # opcodes
    # 0: adv, division, numerator in register A, denominator is 2^(combo operand)
    # 1: bxl, bitwise XOR of register B and literal operand
    # 2: 2: bst: value of combo operand modulo 8, write result to register B
    # 3: 3: jnz, does nothing if a is 0, if a is not zero, then jump literal operand, dont increase instr. pointer by 2
    # 4: bitwise XOR of register B and register C, store result in register B
    # 5: out, calculate combo operand modulo 8, output value on console,
    # 6: works like adv, but store result in register B
    # 7: cdv, 7, works like adv, but store result in register C
    register_a = 0
    register_b = 0
    register_c = 0

    program_input = []

    with open(filename) as file:

        phase = 0
        for line in file:
            line: str = line.replace("\n", "")
            if phase == 0:
                register_a = int(line.replace("Register A: ", ""))
                phase += 1
            elif phase == 1:
                register_b = int(line.replace("Register B: ", ""))
                phase += 1
            elif phase == 2:
                register_c = int(line.replace("Register C: ", ""))
                phase += 1
            elif phase == 3:
                phase += 1
            else:
                program_input = list(map(lambda x: int(x), line.replace("Program: ", "").split(",")))

    registers = [register_a, register_b, register_c]

    solution = solve_rec(program_input, 0, pow(8, len(program_input) - 1), 0)
    print("Solution Day 17 Part 2: ", solution)
