import sys

#read arguements
program_filepath = sys.argv[1]

#####################################################
#####################################################
#            Tokenize Program
#####################################################
#####################################################

#read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    # check for empty line
    if opcode == "":
        continue
        
    # check if it's a label
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]]=token_counter
        continue

    # store the opcode token
    program.append(opcode)
    token_counter += 1

    # handle each opcode
    if opcode == "PUSH":
        # expecting a number
        number = int(parts[1])
        program.append(number)
        token_counter +=1
    elif opcode == "PRINT":
        # parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "JUMP.EQ.0":
        # read label
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "JUMP.GT.0":
        # read label
        label = parts[1]
        program.append(label)
        token_counter += 1


#####################################################
#            Interpreter Program
#####################################################

class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number

    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    def top (self):
        return self.buf[self.sp]
    


pc = 0
Stack = Stack(256)


while program[pc] != "HALT":
    opcode = program[pc]
    pc +=1

    if opcode == "PUSH":
        number = program[pc]
        pc += 1

        Stack.push(number)
    elif opcode == "POP":
        Stack.pop()
    elif opcode == "ADD":
        a = Stack.pop()
        b = Stack.pop()
        Stack.push(a + b)
    elif opcode == "SUB":
        a = Stack.pop()
        b = Stack.pop()
        Stack.push(b - a)
    elif opcode == "PRINT":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "READ":
        number = int(input())
        Stack.push(number)
    elif opcode == "JUMP.EQ.0":
        number = Stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "JUMP.GT.0":
        number = Stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
