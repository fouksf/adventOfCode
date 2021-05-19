import copy
import itertools

input = open("2019/5/input.txt", "r")
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

def sumOp(i, operations, modes):
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
    return 4

def multiplyOp(i, operations, modes):
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
    return 4

def saveOp(i, operations, modes):
    operations[operations[i + 1]] = 4 #TODO: learn how to take input
    return 2

def printOp(i, operations, modes):
    if len(modes) >= 1:
        first_mode = modes[-1]
    else:
        first_mode = '0'
    parameter = get_parameter_value(operations[i + 1], first_mode, operations)
    return parameter

def jumpIfTrueOp(i, operations, modes):
    return jumpOp(i, operations, modes, True)

def jumpIfFalseOp(i, operations, modes):
    return jumpOp(i, operations, modes, False)

def jumpOp(i, operations, modes, isIfTrue):
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
        return second_parameter - i
    else:
        return 3

def lessThanOp(i, operations, modes):
    return compareOp(i, operations, modes, lambda a, b: a < b)

def equalsOp(i, operations, modes):
    return compareOp(i, operations, modes, lambda a, b: a == b)

def compareOp(i, operations, modes, comparator):
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
    return 4

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

def execute_operation(i, operations, opcode, modes):
    function = FUNCTIONS[opcode]
    return function(i, operations, modes)

def run_int_code(operations):
    i = 0
    while i < len(operations):
        modes = str(operations[i])[:-2]
        opcode = int(str(operations[i])[-2:])

        if operations[i] == PRINT:
            return execute_operation(i, operations, opcode, modes)
        else:
            i += execute_operation(i, operations, opcode, modes)
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
example_input = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

print(run_int_code(example_input))

# def run_amplifier(input, phase_setting):
#     input = 
#     run_int_code(operations, input)