answersFile = open("solutions/day6/answers.txt", "r")
groupAnswers = answersFile.read().split("\n\n")
answersFile.close()

def getNumberOfQuestions(group):
    return len(set(group.replace('\n', '')))

def getNumberOfAllYesses(group):
    answers = group.split('\n')
    count = 0
    for letter in answers[0]:
        if group.count(letter) == len(answers):
            count += 1
    return count


result = 0
for group in groupAnswers:
    count = getNumberOfQuestions(group)
    result += count

print(result)

result = 0
for group in groupAnswers:
    count = getNumberOfAllYesses(group)
    result += count

print(result)