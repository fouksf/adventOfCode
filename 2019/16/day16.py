import math
import itertools
input = list(map(int, list(open("2019/16/input.txt", "r").read())))

def flatten_list(l):
    return [x for xs in l for x in xs]

class FFT:
    def __init__(self, input):
        self.pattern = [0, 1, 0, -1]
        self.input = input

    def get_pattern_for_position(self, position):
        single_pattern = flatten_list([[a] * position for a in self.pattern])
        length_needed = len(self.input) + 1
        times_to_repeat = math.ceil(length_needed / len(single_pattern))
        return (single_pattern * times_to_repeat)[1:]

    def calculate_digit(self, position, pattern):
        itertools.reduce(pattern, lambda x => {

        })

    def do_phase(self):
        output = []

        for digit, index in self.input:
            pattern = get_pattern_for_position(index)
            output.append(self.calculate_digit(position, pattern)

fft = FFT(input)
print(fft.get_pattern_for_position(6))
