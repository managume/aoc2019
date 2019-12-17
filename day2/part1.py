
def intcode(program):
    i = 0
    while i < len(program):
        opcode = program[i]
        if opcode == 99:
            print('99: Program finished.')
            return program
        elif opcode == 1:
            pos_input1 = program[i+1]
            pos_input2 = program[i+2]
            pos_output = program[i+3]
            program[pos_output] = program[pos_input1] + program[pos_input2]
        elif opcode == 2:
            pos_input1 = program[i+1]
            pos_input2 = program[i+2]
            pos_output = program[i+3]
            program[pos_output] = program[pos_input1] * program[pos_input2] 
        else:
            print("OPCODE UNKNOWN: %d" % opcode)
            print('ERROR: Unknown opcode was encountered.')
            break
        i+=4


# Restoring gravity assist program:
#   - Replace position 1 with value 12.
#   - Replace position 2 with value 2.
#   - Return position 0 after program halts
program = [int(i) for i in open('input.txt').read().split(',')]
program[1] = 12
program[2] = 2
result = intcode(program)
print(result)
print(program[0])
