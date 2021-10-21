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
            9: self.changeRBOffset
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

    def sumOp(self, modes, input, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[-1])
        v_two = self.get_parameter_value(parameters[1], modes[-2])
        v_three = self.get_parameter_index(parameters[2], modes[0])
        self.instructions[v_three] = v_one + v_two
        self.position += self.parameter_count[1] + 1
        return False

    def multiplyOp(self, modes, input, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[-1])
        v_two = self.get_parameter_value(parameters[1], modes[-2])
        v_three = self.get_parameter_index(parameters[2], modes[0])
        self.instructions[v_three] = v_one * v_two
        self.position += self.parameter_count[2] + 1
        return False

    def saveOp(self, modes, input, parameters):
        v_one = self.get_parameter_index(parameters[0], modes[-1])
        self.instructions[v_one] = input
        self.position += self.parameter_count[3] + 1
        return True

    def printOp(self, modes, input, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[-1])
        self.position += self.parameter_count[4] + 1
        return v_one

    def jumpIfTrueOp(self, modes, input, parameters):
        return self.jumpOp(modes, True, input, parameters)

    def jumpIfFalseOp(self, modes, input, parameters):
        return self.jumpOp(modes, False, input, parameters)

    def jumpOp(self, modes, isIfTrue, input, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[-1])
        v_two = self.get_parameter_value(parameters[1], modes[-2])
        if((v_one != 0 and isIfTrue) or
        (v_one == 0 and not isIfTrue)):
            self.position = v_two
            return False
        else:
            self.position += self.parameter_count[5] + 1
            return False

    def lessThanOp(self, modes, input, parameters):
        usedInput = self.compareOp(modes, lambda a, b: a < b, input, parameters)
        self.position += self.parameter_count[7] + 1
        return usedInput

    def equalsOp(self, modes, input, parameters):
        usedInput = self.compareOp(modes, lambda a, b: a == b, input, parameters)
        self.position += self.parameter_count[8] + 1
        return usedInput

    def compareOp(self, modes, comparator, input, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[-1])
        v_two = self.get_parameter_value(parameters[1], modes[-2])
        v_three = self.get_parameter_index(parameters[2], modes[0])

        if(comparator(v_one, v_two)):
            self.instructions[v_three] = 1
        else:
            self.instructions[v_three] = 0
        return False

    def changeRBOffset(self, modes, input, parameters):
        v_one = self.get_parameter_value(parameters[0], modes[-1])
        self.relative_base_offset += v_one
        self.position += self.parameter_count[9] + 1
        return False

    def find_function(self, opcode):
        if(opcode in self.functions):
            return self.functions[opcode]

    def execute_operation(self, opcode, modes, input, parameters):
        function = self.find_function(opcode)
        return function(modes, input, parameters)

    def run_int_code(self, input):
        if(self.halted == True):
            return self.instructions[0]
        input_index = 0
        while self.position < len(self.instructions):
            modes = str(self.instructions[self.position])[:-2]
            opcode = int(str(self.instructions[self.position])[-2:])
            parameters = self.instructions[self.position + 1: self.position + self.parameter_count[opcode] + 1]

            while len(modes) < self.parameter_count[opcode]:
                modes = "0" + modes
        
            if opcode == Operation.PRINT.value:
                value_to_print = self.execute_operation(opcode, modes, input[input_index], parameters)
                print("printing: ", value_to_print)
            elif opcode == Operation.HALT.value:
                self.halted = True
                return self.instructions[0]
            else:
                used_input = self.execute_operation(opcode, modes, input[input_index], parameters)
                if (used_input):
                    if(input_index < len(input) - 1):
                        input_index += 1
        print("instructions" + self.instructions)
        return self.instructions
