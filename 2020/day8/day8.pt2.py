import copy

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
            raise Exception("Infinite loop found")
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
    return accumulator



def fixProgram(instructions):
    for i in range(0, len(instructions)):
        if instructions[i][0] == ACC:
            continue
        changedInstructions = copy.deepcopy(instructions)
        if instructions[i][0] == NOP:
            changedInstructions[i][0] = JMP
        elif instructions[i][0] == JMP:
            changedInstructions[i][0] = NOP
        else:
            raise Exception(f'Unknow operation {instructions[i][0]}')

        try:
            accumulator = execute(changedInstructions)
            return accumulator
        except: 
            print(f'{i} not successful')





instructions = parseInput()
print(fixProgram(instructions))