rulesFile = open("solutions/day7/rules.txt", "r")
rulesLines = rulesFile.read().split("\n")
rulesFile.close()

MY_BAG = "shiny gold bag"
rules = {}
for rule in rulesLines:
    line = rule.split("s contain ")
    contents = line[1]
    contentMap = {}
    if contents != 'no other bags.':
        contents = contents.replace("bags", "bag").replace(".","").strip().split(", ")
        for color in contents:
            contentMap[color[2:]] = int(color[0:1])
    
    rules[line[0]] = contentMap

def getHowManyBagsInside(bagColour, rules):
    if len(rules[bagColour]) == 0:
        return 0
    result = 0
    for color, count in rules[bagColour].items():
        result += count + count * getHowManyBagsInside(color, rules)

    return result

print(getHowManyBagsInside(MY_BAG, rules))