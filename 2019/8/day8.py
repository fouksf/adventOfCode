input = open("2019/8/input.txt", "r").read()

groups_of_six = [input[i:i+(25*6)] for i in range(0, len(input), (25*6))]
count = []

for group in groups_of_six:
    zeros = group.count('0')
    count.append(zeros)

min_number = min(count)
min_index = count.index(min_number)

min_group = groups_of_six[min_index]
integers = []

for char in min_group:
    integers.append(int(char))

print(integers.count(1) * integers.count(2))
