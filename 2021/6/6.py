input = open("2021/6/input.txt", "r").read().split(",")

class Lanternfish:
    def __init__(self, days_until_spawning):
        self.days_until_spawning = days_until_spawning

    def pass_a_day(self):
        if self.days_until_spawning == 0:
            self.days_until_spawning = 6
            return Lanternfish(8)
        else:
            self.days_until_spawning -= 1
    def __repr__(self):
        return str(self.days_until_spawning)

lanternfish = list(map(lambda l: Lanternfish(int(l)), input))


# for i in range(0, 256):
#     new_fishes = []
#     for fish in lanternfish:
#         puppy_fish = fish.pass_a_day()
#         if puppy_fish:
#             new_fishes.append(puppy_fish)
#     lanternfish += new_fishes



## Part Two

fishes = {int(days):input.count(days) for days in input}
print(fishes)

def pass_a_day(current_day):
    next_day = {}
    for i in range(1, 9):
        if i in current_day:
            next_day[i - 1] = current_day[i]
        else:
            next_day[i - 1] = 0
    if 0 not in current_day:
        current_day[0] = 0
    next_day[8] = current_day[0]
    next_day[6] += current_day[0]
    return next_day

for i in range(0, 256):
    fishes = pass_a_day(fishes)

count = 0
for v in fishes:
    count += fishes[v]

print(count)