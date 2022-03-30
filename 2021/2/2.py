
input = open("2021/2/input.txt", "r").read().split("\n")

class Submarine:
    def __init__(self, position, depth):
        self.position = position
        self.depth = depth
    
    def move(self, command):
        (direction, distance) = command.split(" ")
        if(direction == "up"):
            self.depth -= int(distance)
        elif(direction == "down"):
            self.depth += int(distance)
        elif(direction == "forward"):
            self.position += int(distance)
        else:
            raise Exception(f'Unknown command {direction}')
        print(f'Position: {self.position}, depth: {self.depth}')

# submarine = Submarine(0, 0)
# for command in input:
#     submarine.move(command)

# print(submarine.position * submarine.depth)


class ComplicatedSubmarine:
    def __init__(self, position, depth, aim):
        self.position = position
        self.depth = depth
        self.aim = aim
    
    def move(self, command):
        (direction, distance) = command.split(" ")
        if(direction == "up"):
            self.aim -= int(distance)
        elif(direction == "down"):
            self.aim += int(distance)
        elif(direction == "forward"):
            self.position += int(distance)
            self.depth += (self.aim * int(distance))
        else:
            raise Exception(f'Unknown command {direction}')
        # print(f'Position: {self.position}, depth: {self.depth}')


complicated_submarine = ComplicatedSubmarine(0, 0, 0)
for command in input:
    complicated_submarine.move(command)

print(complicated_submarine.depth * complicated_submarine.position)