
input = list(map(int, open("2021/1/input.txt", "r").read().split("\n")))

changes_count = 0
for i in range(0, len(input) - 1):
    if(input[i] < input[i + 1]):
        changes_count += 1


triple_changes_count = 0
for i in range(0, len(input) - 3):
    if(input[i] < input[i + 3]):
        triple_changes_count += 1

print(triple_changes_count)