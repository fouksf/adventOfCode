from amplifier import Amplifier


input = list(map(int, open("2019/9/input.txt", "r").read().split(",")))
# input = [104,1125899906842624,99]
amplifier = Amplifier(input)
amplifier.run_int_code([1])