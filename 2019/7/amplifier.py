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

class Amplifier:
    def __init__(self, instructions):
        self.instructions = instructions
        self.position = 0
        self.halted = False
        self.FUNCTIONS = {}


    def get_parameter_value(self, parameter, mode):
        if mode == MODES[POSITION]:
            return int(self.instructions[int(parameter)])
        elif mode == MODES[IMMEDIATE]:
            return int(parameter)
        raise Exception(f'Unknown mode {mode}')

    def sumOp(self, modes, input):
        if len(modes) >= 1:
            first_mode = modes[-1]
        else:
            first_mode = '0'
        if len(modes) >= 2:
            second_mode = modes[-2]
        else:
            second_mode = '0'
        first_parameter = self.get_parameter_value(self.instructions[self.position + 1], first_mode)
        second_parameter = self.get_parameter_value(self.instructions[self.position + 2], second_mode)
        sum_index = self.instructions[self.position + 3]
        self.instructions[sum_index] = first_parameter + second_parameter
        return (4, False)

    def multiplyOp(self, modes, input):
        if len(modes) >= 1:
            first_mode = modes[-1]
        else:
            first_mode = '0'
        if len(modes) >= 2:
            second_mode = modes[-2]
        else:
            second_mode = '0'
        first_parameter = self.get_parameter_value(self.instructions[self.position + 1], first_mode)
        second_parameter = self.get_parameter_value(self.instructions[self.position + 2], second_mode) #TODO: leading zero problem
        product_index = self.instructions[self.position + 3]
        self.instructions[product_index] = first_parameter * second_parameter
        return (4, False)

    def saveOp(self, modes, input):
        self.instructions[self.instructions[self.position + 1]] = input 
        return (2, True)

    def printOp(self, modes, input):
        if len(modes) >= 1:
            first_mode = modes[-1]
        else:
            first_mode = '0'
        parameter = self.get_parameter_value(self.instructions[self.position + 1], first_mode)
        return parameter

    def jumpIfTrueOp(self, modes, input):
        return self.jumpOp(modes, True, input)

    def jumpIfFalseOp(self, modes, input):
        return self.jumpOp(modes, False, input)

    def jumpOp(self, modes, isIfTrue, input):
        if len(modes) >= 1:
            first_mode = modes[-1]
        else:
            first_mode = '0'
        if len(modes) >= 2:
            second_mode = modes[-2]
        else:
            second_mode = '0'
        parameter = self.get_parameter_value(self.instructions[self.position + 1], first_mode)
        second_parameter = self.get_parameter_value(self.instructions[self.position + 2], second_mode)
        if((parameter != 0 and isIfTrue) or
        (parameter == 0 and not isIfTrue)):
            return (second_parameter - self.position, False)
        else:
            return (3, False)

    def lessThanOp(self, modes, input):
        return self.compareOp(modes, lambda a, b: a < b, input)

    def equalsOp(self, modes, input):
        return self.compareOp(modes, lambda a, b: a == b, input)

    def compareOp(self, modes, comparator, input):
        if len(modes) >= 1:
            first_mode = modes[-1]
        else:
            first_mode = '0'
        if len(modes) >= 2:
            second_mode = modes[-2]
        else:
            second_mode = '0'
        first_parameter = get_parameter_value(self.instructions[self.position + 1], first_mode, self.instructions)
        second_parameter = get_parameter_value(self.instructions[self.position + 2], second_mode, self.instructions)
        if(comparator(first_parameter, second_parameter)):
            self.instructions[self.instructions[self.position + 3]] = 1
        else:
            self.instructions[self.instructions[self.position + 3]] = 0
        return (4, False)

    def find_function(self, opcode):
        functions = {
            SUM: self.sumOp,
            MULTIPLY: self.multiplyOp,
            SAVE: self.saveOp,
            PRINT: self.printOp,
            JUMP_IF_TRUE: self.jumpIfTrueOp,
            JUMP_IF_FALSE: self.jumpIfFalseOp,
            LESS_THAN: self.lessThanOp,
            EQUALS: self.equalsOp
        }
        if(opcode in functions):
            return functions[opcode]

    def execute_operation(self, opcode, modes, input):
        function = self.find_function(opcode)
        return function(modes, input)

    def run_int_code(self, input):
        if(self.halted == True):
            return input[0]
        operations = self.instructions
        input_index = 0
        while self.position < len(operations):
            modes = str(operations[self.position])[:-2]
            opcode = int(str(operations[self.position])[-2:])

            if operations[self.position] == PRINT:
                value_to_print = self.execute_operation(opcode, modes, input[input_index])
                self.position += 2
                return value_to_print
            elif operations[self.position] == HALT:
                print("in halt")
                self.halted = True
                return input[0]
            else:
                (parameters_consumed, used_input) = self.execute_operation(opcode, modes, input[input_index])
                self.position += parameters_consumed
                if (used_input):
                    if(input_index < len(input) - 1):
                        input_index += 1
            
        return operations[0]
