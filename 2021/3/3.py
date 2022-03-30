input = list(map(list, open("2021/3/input.txt", "r").read().split("\n")))

## Part 1
gamma = ''
epsilon = ''
half = len(input) / 2
for i in range(0, len(input[0])):
    if sum(map(int, [item[i] for item in input])) < half:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

# print(int(gamma, 2) * int(epsilon, 2))

## Part 2

def most_common_in_position(input, position, tie_breaker):
    half = len(input) / 2
    ones = sum(map(int, [item[position] for item in input]))
    if ones < half:
        return '0'
    elif ones > half:
        return '1'
    return tie_breaker


def least_common_in_position(input, position, tie_breaker):
    half = len(input) / 2
    ones = sum(map(int, [item[position] for item in input])) 
    if ones < half:
        return '1'
    elif ones > half:
        return '0'
    return tie_breaker

def filter_with_bit_in_position(input, position, bit_wanted):
    return list(filter(lambda el: el[position] == bit_wanted, input))

def find_oxygen(input):
    i = 0
    while(len(input) > 1):
        most_common = most_common_in_position(input, i, '1')
        input = filter_with_bit_in_position(input, i, most_common)
        i += 1
    return input[0]

def find_co(input):
    i = 0
    while(len(input) > 1):
        least_common = least_common_in_position(input, i, '0')
        input = filter_with_bit_in_position(input, i, least_common)
        i += 1
    return input[0]

print(int(''.join(find_oxygen(input)), 2) * int(''.join(find_co(input)), 2))