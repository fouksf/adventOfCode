geologyFile = open("day3/geology.txt", "r")
geology = geologyFile.read().split("\n")
geologyFile.close()
tree = '#'
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
columnsCount = len(geology[0])
result = 1
for slope in slopes:
    treesCount = 0
    [row, column] = [0,0]
    while row < len(geology):
        if geology[row][column] == tree:
            treesCount += 1
        row += slope[1]
        column = (column + slope[0]) % columnsCount
    result *= treesCount
print(result)
