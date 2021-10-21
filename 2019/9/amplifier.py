from enum import Enum
import copy

# Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
# Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
class Operation(Enum):
    SUM = 1
    MULTIPLY = 2
    SAVE = 3
    PRINT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RB_OFFSET = 9
    HALT = 99

class Mode(Enum):
    POSITION = "0"
    IMMEDIATE = "1"
    RELATIVE = "2"

class Amplifier:
    def __init__(self, instructions):
        self.instructions = copy.deepcopy(instructions) + [0] * 1000
        self.position = 0
        self.relative_base_offset = 0
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
            9: self.changeRBOffset,
            99: self.halt
        }
        self.parameter_count = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            9: 1,
            99: 0
        }
        self.input = []

    def get_parameter_value(self, parameter, mode):
        if mode == Mode.POSITION.value:
            return int(self.instructions[int(parameter)])
        elif mode == Mode.IMMEDIATE.value:
            return int(parameter)
        elif mode == Mode.RELATIVE.value:
            return int(self.instructions[self.relative_base_offset + int(parameter)])
        raise Exception(f'Unknown mode {mode}')

    def get_parameter_index(self, parameter, mode):
        if mode == Mode.POSITION.value:
            return int(parameter)
        elif mode == Mode.IMMEDIATE.value:
            return int(parameter)
        elif mode == Mode.RELATIVE.value:
            return self.relative_base_offset + int(parameter)
        raise Exception(f'Unknown mode {mode}')

    def sumOp(self, modes, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[0])
        v_two = self.get_parameter_value(parameters[1], modes[1])
        v_three = self.get_parameter_index(parameters[2], modes[2])
        self.instructions[v_three] = v_one + v_two
        self.position += self.parameter_count[1] + 1

    def multiplyOp(self, modes, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[0])
        v_two = self.get_parameter_value(parameters[1], modes[1])
        v_three = self.get_parameter_index(parameters[2], modes[2])
        self.instructions[v_three] = v_one * v_two
        self.position += self.parameter_count[2] + 1

    def saveOp(self, modes, parameters):
        v_one = self.get_parameter_index(parameters[0], modes[-1])
        self.instructions[v_one] = self.input.pop()
        self.position += self.parameter_count[3] + 1

    def printOp(self, modes, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[-1])
        print("printing: ", v_one)
        self.position += self.parameter_count[4] + 1

    def jumpIfTrueOp(self, modes, parameters):
        self.jumpOp(modes, True, parameters)

    def jumpIfFalseOp(self, modes, parameters):
        self.jumpOp(modes, False, parameters)

    def jumpOp(self, modes, isIfTrue, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[0])
        v_two = self.get_parameter_value(parameters[1], modes[1])
        if((v_one != 0 and isIfTrue) or
        (v_one == 0 and not isIfTrue)):
            self.position = v_two
        else:
            self.position += self.parameter_count[5] + 1

    def lessThanOp(self, modes, parameters):
        self.compareOp(modes, lambda a, b: a < b, parameters)
        self.position += self.parameter_count[7] + 1

    def equalsOp(self, modes, parameters):
        self.compareOp(modes, lambda a, b: a == b, parameters)
        self.position += self.parameter_count[8] + 1

    def compareOp(self, modes, comparator, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[0])
        v_two = self.get_parameter_value(parameters[1], modes[1])
        v_three = self.get_parameter_index(parameters[2], modes[2])

        if(comparator(v_one, v_two)):
            self.instructions[v_three] = 1
        else:
            self.instructions[v_three] = 0

    def changeRBOffset(self, modes, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[-1])
        self.relative_base_offset += v_one
        self.position += self.parameter_count[9] + 1

    def halt(self, modes, parameters):
        self.halted = True

    def find_function(self, opcode):
        if(opcode in self.functions):
            return self.functions[opcode]

    def execute_operation(self, opcode, modes, parameters):
        function = self.find_function(opcode)
        return function(modes, parameters)

    def run_int_code(self, input):
        self.input = input

        while self.position < len(self.instructions):
            if self.halted:
                return self.instructions[0]

            modes = str(self.instructions[self.position])[:-2][::-1]
            opcode = int(str(self.instructions[self.position])[-2:])
            parameters = self.instructions[self.position + 1: self.position + self.parameter_count[opcode] + 1]

            while len(modes) < self.parameter_count[opcode]:
                modes += "0"

            self.execute_operation(opcode, modes, parameters)
