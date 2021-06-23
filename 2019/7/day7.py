import copy
import itertools
import math
from amplifier import Amplifier

input = open("2019/7/input.txt", "r")
int_operations = list(map(int, input.read().split(",")))

phases = [9, 8, 7, 6, 5]
# iterations = itertools.permutations(phases)
example_input = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
iterations = [[9,8,7,6,5]]
# print(run_int_code(example_input))

outputs = []
for iteration in iterations:
    old_input_signal = 0
    input_signal = 0
    amps = {}

    while True:
        for amplifier in range(1, 6):
            if amplifier not in amps:
                amps[amplifier] = Amplifier(example_input)
                input = [iteration[amplifier - 1], input_signal]
            else:
                input = [input_signal]
            amp = amps[amplifier]
            old_input_signal = copy.deepcopy(input_signal)
            input_signal = amp.run_int_code(input)
            print("amplifier " +  str(amplifier) + " got input: " + str(input_signal))

            if (input_signal == False):
                input_signal = old_input_signal
                print(input)
                print(old_input_signal)
                break
    
    outputs.append(old_input_signal)

print(outputs)
print(max(outputs))