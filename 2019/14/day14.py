import math

input = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

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

while len(materials_needed) > 0:
    new_materials = {}
    for material in materials_needed:
        print(materials_needed)
        reaction = instructions[reacts[material]]
        needed = reaction.split(" => ")[0].split(", ")
        amount_needed = materials_needed[material]
        for need in needed:
            (amount, element) = need.split(" ")
            if element == "ORE":
                amount_created = int(reaction.split(" => ")[1].split(" ")[0])
                first_thing = math.ceil(amount_needed / amount_created)
                ore_count += first_thing * int(amount)
                continue

            if element in new_materials:
                new_materials[element] += (amount_needed * int(amount))
            else:
                new_materials[element] = (amount_needed * int(amount))
        
    materials_needed = new_materials

print(ore_count)
