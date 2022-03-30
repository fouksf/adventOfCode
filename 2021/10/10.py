input = open("2021/10/input.txt", "r").read().split("\n")

def score_a_wrong_line(line):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for bracket in line:
        if bracket in brackets:
            stack.append(bracket)
        else:
            if brackets[stack[-1]] == bracket:
                stack.pop()
            else:
                return scores[bracket]
    return 0

def score_incomplete_line(line):
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for bracket in line:
        if bracket in brackets:
            stack.append(bracket)
        else:
            if brackets[stack[-1]] == bracket:
                stack.pop()
            else:
                return 0
    if len(stack) == 0:
        raise Exception("WTF")

    stack.reverse()
    return calculate_score_for_remaining_brackets(stack)

def calculate_score_for_remaining_brackets(brackets):
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    for bracket in brackets:
        score = score * 5 + scores[bracket]
    return score


scores = []
for line in input:
    score = score_incomplete_line(line)
    if score != 0:
        scores.append(score)

scores = sorted(scores)
middle = len(scores)//2
print(scores[middle])
