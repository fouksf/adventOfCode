import sys, re

required = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" }

pattern1, pattern2 = re.compile("#\w{6}"), re.compile("(\d+)(cm|in)")

def existence(f): return required.issubset(fields)

def validate(f):
    if not (len(f["byr"]) == 4 and 1920 <= int(f["byr"]) <= 2002): return False
    if not (len(f["iyr"]) == 4 and 2010 <= int(f["iyr"]) <= 2020): return False
    if not (len(f["eyr"]) == 4 and 2020 <= int(f["eyr"]) <= 2030): return False
    if not (len(f["pid"]) == 9): return False
    if not f["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}: return False
    if not re.fullmatch(pattern1, f["hcl"]): return False
    if not (height := re.fullmatch(pattern2, f["hgt"])): return False
    hgt, unit = height.groups()
    if unit == "cm": return 150 <= int(hgt) <= 193
    elif unit == "in": return 59 <= int(hgt) <= 76

count = 0
passportsFile = open("solutions/day4/passports.txt", "r")
passports = passportsFile.read().split("\n\n")
for p in passports:
    fields = {k: v for k, v in (f.split(":") for f in p.split())}
    count += existence(set(fields.keys())) and validate(fields)

print(count)