import copy
import itertools
import math
from amplifier import Amplifier


# example_input = open("2019/7/input.txt", "r")
# int_operations = list(map(int, example_input.read().split(",")))

phases = [9, 8, 7, 6, 5]
# iterations = itertools.permutations(phases)
example_opcodes = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
# example_input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,6,23,2,6,23,27,2,27,9,31,1,5,31,35,1,35,10,39,2,39,9,43,1,5,43,47,2,47,10,51,1,51,6,55,1,5,55,59,2,6,59,63,2,63,6,67,1,5,67,71,1,71,9,75,2,75,10,79,1,79,5,83,1,10,83,87,1,5,87,91,2,13,91,95,1,95,10,99,2,99,13,103,1,103,5,107,1,107,13,111,2,111,9,115,1,6,115,119,2,119,6,123,1,123,6,127,1,127,9,131,1,6,131,135,1,135,2,139,1,139,10,0,99,2,0,14,0]
iterations = [[1,0,4,3,2]]
# print(run_int_code(example_input))

outputs = []
for iteration in iterations:
    output_signal = 0
    input_signal = 0
    amplifiers = {}

    while True:
        for ampNumber in range(1, 6):
            if ampNumber not in amplifiers:
                amplifiers[ampNumber] = Amplifier(example_opcodes)
                input = [iteration[ampNumber - 1], input_signal]
            else:
                input = [input_signal]
            current_amplifier = amplifiers[ampNumber]
            output_signal = current_amplifier.run_int_code(input)
            print("amplifier " +  str(ampNumber) + " gave output: " + str(output_signal))
            input_signal = output_signal
            if (output_signal == False):
                print(input)
                print("what are we doing here?")
                print("looks like amplifier" + ampNumber + " has halted")
                break
    
    outputs.append(output_signal)

print(outputs)
print(max(outputs))

# amplifier = Amplifier([1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,9,19,23,2,13,23,27,1,6,27,31,2,6,31,35,2,13,35,39,1,39,10,43,2,43,13,47,1,9,47,51,1,51,13,55,1,55,13,59,2,59,13,63,1,63,6,67,2,6,67,71,1,5,71,75,2,6,75,79,1,5,79,83,2,83,6,87,1,5,87,91,1,6,91,95,2,95,6,99,1,5,99,103,1,6,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0])
# signal = amplifier.run_int_code([1])
# print(signal)



## last thing I did is some experiments that part 1 works... it does