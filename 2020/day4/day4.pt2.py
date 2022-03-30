import re
passportsFile = open("solutions/day4/passports.txt", "r")
lines = passportsFile.read().split("\n\n")
passports = list(map(lambda passport: passport.replace('\n', ' ').strip(), lines))
passportsFile.close()

def isValid(passport):
    return (passport.count(' ') == 7 or
    (passport.count(' ') == 6 and passport.count('cid:') == 0))

def hasValidValues(passport):
    return (re.search("byr:(19[2-9][0-9]|2000|2001|2002)", passport) != None and
    re.search("iyr:(201[0-9]|2020)", passport) != None and
    re.search("eyr:(202[0-9]|2030)", passport) != None and
    re.search("hgt:(59in|[6][0-9]in|[7][0-6]in|[1][5-8][0-9]cm|[1][9][0-3]cm)", passport) != None and
    re.search("hcl:#[0-9a-f]{6}", passport) != None and
    re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport) != None and
    re.search("pid:(\d){9}($| )", passport) != None )

count = 0
for passport in passports:
    if isValid(passport) and hasValidValues(passport) and brute(passport):
        print(passport)
        count += 1

print(count)
