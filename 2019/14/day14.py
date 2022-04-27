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

materials_stash = {}

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
        print("needed:", materials_needed)
        reaction = instructions[reacts[material]] # 7 A, 1 D => 1 E
        needed = reaction.split(" => ")[0].split(", ") # ["7 A", "1 D"]
        amount_needed = materials_needed[material] # integer eg 1 for FUEL at the start
        amount_created = int(reaction.split(" => ")[1].split(" ")[0])
        for need in needed:
            # amount_of_needed_in_stash = materials_stash[need]
            (amount, element) = need.split(" ")

            excess = amount_created - amount_needed
            if excess > 0:
                if element in materials_stash:
                    materials_stash[element] += excess
                else:
                    materials_stash[element] = excess

            if element == "ORE":
                reaction_run_count = math.ceil(amount_needed / amount_created)
                ore_count += reaction_run_count * int(amount)
                continue

            print("stash:", materials_stash)
            
            if element in new_materials:
                new_materials[element] += (amount_needed * int(amount))
            else:
                new_materials[element] = (amount_needed * int(amount))
        
    materials_needed = new_materials

print(ore_count)
