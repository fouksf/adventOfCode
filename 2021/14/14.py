import math

def parse_input(file_name):
    (template, insertions) = open(file_name, "r").read().split('\n\n')
    insertions = list(
        map(
            lambda i: i.split(' -> '), insertions.split('\n')))
    tuples = {template[i:i + 2]: template.count(template[i:i + 2]) for i in range(0, len(template) - 1)}
    return (tuples, {insertion[0]: insertion[1] for insertion in insertions}) 

(tuples, insertions) = parse_input("2021/14/input.txt")

def do_insertions(tuples, insertions):
    new_tuples = {}
    for k in tuples:
        insertion = insertions[k]
        if k[0] + insertion not in new_tuples:
            new_tuples[k[0] + insertion] = 0
        if insertion + k[1] not in new_tuples:
            new_tuples[insertion + k[1]] = 0
        new_tuples[k[0] + insertion] += tuples[k]
        new_tuples[insertion + k[1]] += tuples[k]
    return new_tuples
    
def do_multiple_steps(tuples, insertions, n):
    for i in range(0, n):
        tuples = do_insertions(tuples, insertions)
    return tuples

def count_occurrences(tuples):
    counts = {}
    for tuple in tuples:
        if tuple[0] not in counts:
            counts[tuple[0]] = 0
        if tuple[1] not in counts:
            counts[tuple[1]] = 0
        counts[tuple[0]] += tuples[tuple]
        counts[tuple[1]] += tuples[tuple]
    return {letter: math.ceil(counts[letter] / 2) for letter in counts}

def find_subtraction(occurrences):
    counts = list(occurrences.values())
    return max(counts) - min(counts)

print(find_subtraction(count_occurrences(do_multiple_steps(tuples, insertions, 40))))