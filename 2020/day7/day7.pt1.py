rulesFile = open("solutions/day7/rules.txt", "r")
rulesLines = rulesFile.read().split("\n")
rulesFile.close()

MY_BAG = "shiny gold bag"
rules = {}
for rule in rulesLines:
    line = rule.split("s contain ")
    rules[line[0]] = line[1]

def getBagsContaining(bagColour, rules):
    bagsContaining = set()
    for key, value in rules.items():
        if key != bagColour and value.find(bagColour) != -1:
            bagsContaining.add(key)
    return bagsContaining

def getPossibleBags(bagColour, rules, checkedColours, coloursContaining):
    if bagColour == 'no other bags.' or bagColour in checkedColours:
        return set()

    coloursContaining.update(getBagsContaining(bagColour, rules))
    checkedColours.add(bagColour)


    coloursToAdd = set()
    for colour in coloursContaining:
         coloursToAdd.update(getPossibleBags(colour, rules, checkedColours, coloursContaining.copy()))

    return coloursContaining.union(coloursToAdd)



print(len(getPossibleBags(MY_BAG, rules, set(), set())))