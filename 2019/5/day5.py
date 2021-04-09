input = open("2019/5/input.txt", "r")
int_operations = input.read().split(",")

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
    POSITION: 0,
    IMMEDIATE: 1
}

def get_parameter_value(parameter, mode, operations):
    if mode == MODES[POSITION]:
        return int(operations[int(parameter)])
    elif mode == MODES[IMMEDIATE]:
        return int(parameter)
    raise Exception('Unknown mode ${mode}')

def sum(i, operations, modes):
    first_parameter = get_parameter_value(operations[i + 1], modes[-1], operations)
    second_parameter = get_parameter_value(operations[i + 2], modes[-2], operations)
    sum_index = operations[i + 3]
    operations[sum_index] = first_parameter + second_parameter
    return 4

def multiply(i, operations, modes):
    first_parameter = get_parameter_value(operations[i + 1], modes[-1], operations)
    second_parameter = get_parameter_value(operations[i + 2], modes[-2], operations) #TODO: leading zero problem
    product_index = operations[i + 3]
    operations[sum_index] = first_parameter * second_parameter
    return 4

def save(i, operations, modes):
    parameter = get_parameter_value(operations[i + 1], 0, operations)
    operations[parameter] = 1 #TODO: learn how to take input
    return 2

def print(i, operations, modes):
    parameter = get_parameter_value(operations[i + 1], modes[-1], operations)
    print(operations[parameter])
    return 2

FUNCTIONS = {
    SUM: sum,
    MULTIPLY: multiply,
    SAVE: save,
    PRINT: print
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
            modes = operations[i][:-2]
            opcode = int(operations[i][-2:])
            i += execute_operation(i, operations, opcode, modes)
    return operations[0]


print(run_int_code(int_operations))