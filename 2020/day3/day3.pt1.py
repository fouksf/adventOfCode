geologyFile = open("day3/geology.txt", "r")
geology = geologyFile.read().split("\n")
geologyFile.close()
tree = '#'
columnsCount = len(geology[0])
[row, column] = [0,0]
treesCount = 0
while row < len(geology):
    if geology[row][column] == tree:
        treesCount += 1
    row += 1
    column = (column + 3) % columnsCount

print(treesCount)
