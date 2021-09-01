input = open("2019/8/input.txt", "r").read()
# input = "0222112222120000"

size = 25*6
# size = 2*2
layers = [input[i:i+(size)] for i in range(0, len(input), (size))]

count = []

for group in layers:
    zeros = group.count('0')
    count.append(zeros)

min_number = min(count)
min_index = count.index(min_number)

min_group = layers[min_index]
integers = []

for char in min_group:
    integers.append(int(char))

pixel_array = []

for pixel in range(size):
    all_pixels = input[pixel::size]
    stripped = all_pixels.replace('2', '')

    if len(stripped) == 0:
        colour = 2
    else:
        colour = int(stripped[0])

    pixel_array.append(colour)

for row in range(0, 6):
    print(pixel_array[row*25:(row*25)+25])