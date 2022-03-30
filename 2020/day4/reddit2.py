def is_Valid(p_field):

    p_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    field, val = p_field.split(":")

    if field not in p_fields:
        return False
    elif field == "byr":
        if 1920 > int(val) or int(val) > 2002:
            return False
    elif field == "iyr":
        if 2010 > int(val) or int(val) > 2020:
            return False
    elif field == "eyr":
        if 2020 > int(val) or int(val) > 2030:
            return False
    elif field == "hcl":
        if val[0] != "#":
            return False
        if len(val) != 7:
            return False
        for i in val[1:]:
            if i not in "1234567890abcdef":
                return False
    elif field == "hgt":
        if val[-2:] == "cm":
            if int(val[0:-2]) < 150 or int(val[0:-2]) > 193:
                return False
        elif val[-2:] == "in":
            if int(val[0:-2]) < 59 or int(val[0:-2]) > 76:
                return False
        else:
            return False
    elif field == "ecl":
        valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if val not in valid_ecl:
            return False
    elif field == "pid":
        if len(val) != 9 or val.isnumeric() == False:
            return False
    elif field == "cid":
        pass
    return True

total_valid = 0
valid_passwords = []
invalid_passwords = []

for passport in open('solutions/day4/passports.txt').read().split("\n\n"):
    valid = 0
    has_cid = False
    for field in passport.strip().split():
        if is_Valid(field):
            valid += 1
            if field.split(":")[0] == 'cid':
                has_cid = True        
    if valid == 8:
        total_valid += 1
        valid_passwords.append(passport)
    elif valid == 7 and not has_cid:
        valid_passwords.append(passport)
        total_valid += 1
    else:
        invalid_passwords.append(passport)        

print('Valid passports:',len(valid_passwords))