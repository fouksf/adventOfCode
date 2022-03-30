passwordsFile = open("passwords.txt", "r")
validPasswordsCount = 0
for line in passwordsFile.read().split('\n'):
    [rule, password] = line.split(':')
    [count, letter] = rule.split(' ')
    [min, max] = map(int, count.split('-'))
    if (password[max] == letter or password[min] == letter) and password[min] != password[max]:
        validPasswordsCount+=1

print(validPasswordsCount)
passwordsFile.close()