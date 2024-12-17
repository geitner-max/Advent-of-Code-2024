
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

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

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

    program = []
    ip = 0

    with open(filename) as file:
        output = []

        phase = 0
        for line in file:
            line: str = line.replace("\n", "")
            if phase == 0:
                register_a = int(line.replace("Register A: ", ""))
                phase +=1
            elif phase == 1:
                register_b = int(line.replace("Register B: ", ""))
                phase += 1
            elif phase == 2:
                register_c = int(line.replace("Register C: ", ""))
                phase += 1
            elif phase == 3:
                phase += 1
            else:
                program = list(map(lambda x: int(x), line.replace("Program: ", "").split(",")))

    registers = [register_a, register_b, register_c]

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
            output.append(str(val))
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

    output_line = ",".join(output)

    print("Solution Day 17 Part 1: ", output_line)
