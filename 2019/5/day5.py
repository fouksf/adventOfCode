input = open("2019/5/input.txt", "r")
int_operations = list(map(int, input.read().split(",")))

SUM = 1
MULTIPLY = 2
SAVE = 3
PRINT = 4
HALT = 99

POSITION = "POSITION"
IMMEDIATE = "IMMEDIATE"

OPERATIONS = {
    SUM: 3,
    MULTIPLY: 3,
    SAVE: 1,
    PRINT: 1
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
    operations[operations[i + 1]] = 1 #TODO: learn how to take input
    return 2

def printOp(i, operations, modes):
    if len(modes) >= 1:
        first_mode = modes[-1]
    else:
        first_mode = '0'
    parameter = get_parameter_value(operations[i + 1], first_mode, operations)
    print(parameter)
    return 2

FUNCTIONS = {
    SUM: sumOp,
    MULTIPLY: multiplyOp,
    SAVE: saveOp,
    PRINT: printOp
}

def execute_operation(i, operations, opcode, modes):
    function = FUNCTIONS[opcode]
    return function(i, operations, modes)

def run_int_code(operations):
    i = 0
    while i < len(operations):
        if operations[i] == HALT:
            break
        else:
            modes = str(operations[i])[:-2]
            opcode = int(str(operations[i])[-2:])
            i += execute_operation(i, operations, opcode, modes)
    return operations[0]

print(run_int_code(int_operations))