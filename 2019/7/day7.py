import copy
import itertools
import math

input = open("2019/7/input.txt", "r")
int_operations = list(map(int, input.read().split(",")))

SUM = 1
MULTIPLY = 2
SAVE = 3
PRINT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
HALT = 99

POSITION = "POSITION"
IMMEDIATE = "IMMEDIATE"

OPERATIONS = {
    SUM: 3,
    MULTIPLY: 3,
    SAVE: 1,
    PRINT: 1,
    JUMP_IF_TRUE: 2,
    JUMP_IF_FALSE: 2,
    LESS_THAN: 3,
    EQUALS: 3
}

MODES = {
    POSITION: '0',
    IMMEDIATE: '1'
}

def get_parameter_value(parameter, mode, operations):
    if mode == MODES[POSITION]:
        return int(operations[int(parameter)])
    elif mode == MODES[IMMEDIATE]:
        return int(parameter)
    raise Exception(f'Unknown mode {mode}')

def sumOp(i, operations, modes, input):
    if len(modes) >= 1:
        first_mode = modes[-1]
    else:
        first_mode = '0'
    if len(modes) >= 2:
        second_mode = modes[-2]
    else:
        second_mode = '0'
    first_parameter = get_parameter_value(operations[i + 1], first_mode, operations)
    second_parameter = get_parameter_value(operations[i + 2], second_mode, operations)
    sum_index = operations[i + 3]
    operations[sum_index] = first_parameter + second_parameter
    return (4, False)

def multiplyOp(i, operations, modes, input):
    if len(modes) >= 1:
        first_mode = modes[-1]
    else:
        first_mode = '0'
    if len(modes) >= 2:
        second_mode = modes[-2]
    else:
        second_mode = '0'
    first_parameter = get_parameter_value(operations[i + 1], first_mode, operations)
    second_parameter = get_parameter_value(operations[i + 2], second_mode, operations) #TODO: leading zero problem
    product_index = operations[i + 3]
    operations[product_index] = first_parameter * second_parameter
    return (4, False)

def saveOp(i, operations, modes, input):
    operations[operations[i + 1]] = input 
    return (2, True)

def printOp(i, operations, modes, input):
    if len(modes) >= 1:
        first_mode = modes[-1]
    else:
        first_mode = '0'
    parameter = get_parameter_value(operations[i + 1], first_mode, operations)
    return parameter

def jumpIfTrueOp(i, operations, modes, input):
    return jumpOp(i, operations, modes, True, input)

def jumpIfFalseOp(i, operations, modes, input):
    return jumpOp(i, operations, modes, False, input)

def jumpOp(i, operations, modes, isIfTrue, input):
    if len(modes) >= 1:
        first_mode = modes[-1]
    else:
        first_mode = '0'
    if len(modes) >= 2:
        second_mode = modes[-2]
    else:
        second_mode = '0'
    parameter = get_parameter_value(operations[i + 1], first_mode, operations)
    second_parameter = get_parameter_value(operations[i + 2], second_mode, operations)
    if((parameter != 0 and isIfTrue) or
    (parameter == 0 and not isIfTrue)):
        return (second_parameter - i, False)
    else:
        return (3, False)

def lessThanOp(i, operations, modes, input):
    return compareOp(i, operations, modes, lambda a, b: a < b, input)

def equalsOp(i, operations, modes, input):
    return compareOp(i, operations, modes, lambda a, b: a == b, input)

def compareOp(i, operations, modes, comparator, input):
    if len(modes) >= 1:
        first_mode = modes[-1]
    else:
        first_mode = '0'
    if len(modes) >= 2:
        second_mode = modes[-2]
    else:
        second_mode = '0'
    first_parameter = get_parameter_value(operations[i + 1], first_mode, operations)
    second_parameter = get_parameter_value(operations[i + 2], second_mode, operations)
    if(comparator(first_parameter, second_parameter)):
        operations[operations[i+3]] = 1
    else:
        operations[operations[i+3]] = 0
    return (4, False)

FUNCTIONS = {
    SUM: sumOp,
    MULTIPLY: multiplyOp,
    SAVE: saveOp,
    PRINT: printOp,
    JUMP_IF_TRUE: jumpIfTrueOp,
    JUMP_IF_FALSE: jumpIfFalseOp,
    LESS_THAN: lessThanOp,
    EQUALS: equalsOp
}

def execute_operation(i, operations, opcode, modes, input):
    function = FUNCTIONS[opcode]
    return function(i, operations, modes, input)

def run_int_code(operations, input):
    i = 0
    input_index = 0
    while i < len(operations):
        modes = str(operations[i])[:-2]
        opcode = int(str(operations[i])[-2:])

        if operations[i] == PRINT:
            return execute_operation(i, operations, opcode, modes, input[input_index])
        else:
            (parameters_consumed, used_input)= execute_operation(i, operations, opcode, modes, input[input_index])
            i += parameters_consumed
            if (used_input):
                if(input_index < len(input) - 1):
                    input_index += 1
            
    return operations[0]

# print(run_int_code(int_operations))

# input: 0
# output: 4,3,2,1,0

# TODO:
# work out how to get output from the int computer - done
# work out how to give our int computer input in general
# generate permutations - done

# this_input = copy.deepcopy(input)
phases = [4, 3, 2, 1, 0]
iterations = itertools.permutations(phases)
example_input = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

# print(run_int_code(example_input))
outputs = []
for iteration in iterations:
    input_signal = 0
    for amplifier in range(1, 6):
        instructions = copy.deepcopy(int_operations)
        input = [iteration[amplifier - 1], input_signal]
        input_signal = run_int_code(instructions, input)
    
    outputs.append(input_signal)

print(outputs)
print(max(outputs))