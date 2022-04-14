input = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

instructions = input.split("\n")
materials_needed = {
    "FUEL": 1
}
ore_count = 0

def build_mapping():
    reactions = {}
    for i, line in enumerate(instructions):
        end = line.split(" => ")[1]
        mat = end.split(" ")[1]
        reactions[mat] = i
    return reactions

reacts = build_mapping()

for material in materials_needed:
    print(materials_needed)
    reaction = instructions[reacts[material]]
    needed = reaction.split(", ")
    print(needed)
    for need in needed:
        stuff = need.split(" ")
        print(stuff)
        amount = stuff[0]
        name = stuff[1]
        if name == "ORE":
            ore_count += int(amount)
            continue

        if name in materials_needed:
            materials_needed[name] += int(amount)
        else:
            materials_needed[name] = int(amount)
    
    del materials_needed[needed]
