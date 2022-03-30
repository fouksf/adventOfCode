passportsFile = open("solutions/day4/passports.txt", "r")
lines = passportsFile.read().split("\n\n")
passports = list(map(lambda passport: passport.replace('\n', ' ').strip(), lines))
passportsFile.close()

def isValid(passport):
    return (passport.count(' ') == 7 or
    (passport.count(' ') == 6 and passport.count('cid:') == 0))


count = 0
for passport in passports:
    if isValid(passport):
        count += 1


print(count)