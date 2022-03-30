
input = open("2021/8/input.txt", "r").read().split("\n")

# a = list(map(lambda l: l.split("|")[1], input))
# b = list(map(lambda x: x.split(), a))
# c = list(map(lambda x: sum(list(map(lambda y: 1 if len(y) != 5 and len(y) != 6 else 0, x))), b))
# d = sum(c)
# print(d)


class Segment:
    def __init__(self, digits):
        one = next(filter(lambda d: len(d) == 2, digits))
        seven = next(filter(lambda d: len(d) == 3, digits))
        four = next(filter(lambda d: len(d) == 4, digits))
        eight = next(filter(lambda d: len(d) == 7, digits))
        nine = next(filter(lambda d: len(d) == 6 and contains(d, four), digits))
        zero = next(filter(lambda d: len(d) == 6 and d != nine and contains(d, one), digits))
        six = next(filter(lambda d: len(d) == 6 and d != zero and d != nine, digits))
        five = next(filter(lambda d: len(d) == 5 and contains(six, d), digits))
        three = next(filter(lambda d: len(d) == 5 and contains(d, one), digits))
        two = next(filter(lambda d: len(d) == 5 and d != three and d != five, digits))
        self.digits = {
            one: 1,
            two: 2,
            three: 3,
            four: 4,
            five: 5,
            six: 6,
            seven: 7,
            eight: 8,
            nine: 9,
            zero: 0
        }
    
    def read_display(self, wires):
        return 1000 * self.digits[wires[0]] + 100 * self.digits[wires[1]] + 10 * self.digits[wires[2]] + self.digits[wires[3]]


def contains(sett, subsett):
    return set(subsett).issubset(set(sett))

def sort_array_elements(array):
    return list(map(lambda a: ''.join(sorted(a)), array))

sum = 0
for line in input:
    (digits, number) = line.split("|")
    segment = Segment(sort_array_elements(digits.split()))
    sum += segment.read_display(sort_array_elements(number.split()))

print(sum)
        
