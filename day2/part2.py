import sys

def init(noun, verb, filename):
    computer = {
        "noun": noun,
        "verb": verb,
        "pc" : 0,
        "program" : [int(value) for value in open(filename).read().split(',')]
    }
    return computer

def run(c):
    c["program"][1] = c["noun"]
    c["program"][2] = c["verb"]
    pc = c["pc"]

    opcode = c["program"][pc]
    pos_input1 = c["program"][pc+1]
    pos_input2 = c["program"][pc+2]
    pos_output = c["program"][pc+3]

    input1 = c["program"][pos_input1]
    input2 = c["program"][pos_input2]

    if opcode == 99:
        return
    if opcode == 1:
        output = input1 + input2
        c["program"][pos_output] = output
    if opcode == 2:
        output = input1 * input2
        c["program"][pos_output] = output
    c["pc"] += 4
    run(c)
    
def result(c):
    return c["program"][0]

def main(noun,verb,filename):
    c = init(noun,verb,filename)
    run(c)
    return result(c)

def search_result(expectation,filename):
    for n in range(100):
        for v in range(100):
            if main(n,v,filename) == expectation:
                return n,v

#print(main(12,2,'input.txt'))
sol = search_result(19690720,'input.txt')
print(100 * sol[0] + sol[1])


