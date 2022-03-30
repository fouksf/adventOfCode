ACC = "acc"
JMP = "jmp"
NOP = "nop"

def parseLine(line):
    instruction = line.split(" ")
    return [instruction[0], int(instruction[1])]

def parseInput():
    instructionsFile = open("solutions/day8/instructions.txt", "r")
    instructions = list(map(parseLine, instructionsFile.read().split("\n")))
    instructionsFile.close()
    return instructions

def execute(instructions):
    executedLines = set()
    accumulator = 0
    i = 0
    while i < len(instructions):
        if i in executedLines:
            return accumulator
        executedLines.add(i)
        instruction = instructions[i]
        if instruction[0] == ACC:
            accumulator += instruction[1]
            i += 1
        elif instruction[0] == JMP:
            i += instruction[1]
        elif instruction[0] == NOP:
            i += 1
        else:
            raise Exception(f'Unknown operation {instruction[0]}')
    raise Exception("No infinite loop found")
instructions = parseInput()
print(execute(instructions))