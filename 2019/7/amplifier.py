from enum import Enum

class Operation(Enum):
    SUM = 1
    MULTIPLY = 2
    SAVE = 3
    PRINT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 99

class Mode(Enum):
    POSITION = "0"
    IMMEDIATE = "1"

class Amplifier:
    def __init__(self, instructions):
        self.instructions = instructions
        self.position = 0
        self.halted = False
        self.functions = {
            1: self.sumOp,
            2: self.multiplyOp,
            3: self.saveOp,
            4: self.printOp,
            5: self.jumpIfTrueOp,
            6: self.jumpIfFalseOp,
            7: self.lessThanOp,
            8: self.equalsOp,
        }

    def get_parameter_value(self, parameter, mode):
        if mode == Mode.POSITION.value:
            return int(self.instructions[int(parameter)])
        elif mode == Mode.IMMEDIATE.value:
            return int(parameter)
        raise Exception(f'Unknown mode {mode}')

    def get_parameters(self, modes):
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
        return (first_parameter, second_parameter)

    def sumOp(self, modes, input):
        parameters = self.get_parameters(modes)
        sum_index = self.instructions[self.position + 3]
        self.instructions[sum_index] = parameters[0] + parameters[1]
        return (4, False)

    def multiplyOp(self, modes, input):
        parameters = self.get_parameters(modes)
        product_index = self.instructions[self.position + 3]
        self.instructions[product_index] = parameters[0] * parameters[1]
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
        parameters = self.get_parameters(modes)
        if((parameters[0] != 0 and isIfTrue) or
        (parameters[0] == 0 and not isIfTrue)):
            return (parameters[1] - self.position, False)
        else:
            return (3, False)

    def lessThanOp(self, modes, input):
        return self.compareOp(modes, lambda a, b: a < b, input)

    def equalsOp(self, modes, input):
        return self.compareOp(modes, lambda a, b: a == b, input)

    def compareOp(self, modes, comparator, input):
        parameters = self.get_parameters(modes)
        if(comparator(parameters[0], parameters[1])):
            self.instructions[self.instructions[self.position + 3]] = 1
        else:
            self.instructions[self.instructions[self.position + 3]] = 0
        return (4, False)

    def find_function(self, opcode):
        if(opcode in self.functions):
            return self.functions[opcode]

    def execute_operation(self, opcode, modes, input):
        function = self.find_function(opcode)
        return function(modes, input)

    def run_int_code(self, input):
        if(self.halted == True):
            return input[0]
        input_index = 0
        while self.position < len(self.instructions):
            modes = str(self.instructions[self.position])[:-2]
            opcode = int(str(self.instructions[self.position])[-2:])

            if self.instructions[self.position] == Operation.PRINT:
                value_to_print = self.execute_operation(opcode, modes, input[input_index])
                self.position += 2
                return value_to_print
            elif self.instructions[self.position] == Operation.HALT:
                print("in halt")
                self.halted = True
                return input[0]
            else:
                (parameters_consumed, used_input) = self.execute_operation(opcode, modes, input[input_index])
                self.position += parameters_consumed
                if (used_input):
                    if(input_index < len(input) - 1):
                        input_index += 1
            
        return self.instructions[0]
