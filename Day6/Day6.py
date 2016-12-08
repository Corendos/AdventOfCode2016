
# Return the list of each line composing the corrupted message
def readMessageFromFile(filename):
    messages = []
    f = open(filename, 'r')
    for line in f:
        messages.append(line[:len(line) - 1])
    return messages

# Count the frequency of each letter
def countLetter(str):
    L = [(chr(i), 0) for i in range(97, 97 + 26)]
    for c in str:
        L[ord(c) - 97] = (L[ord(c) - 97][0],L[ord(c) - 97][1] + 1)
    return L

# Return a list of list of tuple giving the letter frequency for each input string
def getFrequencyFromMessages(messages):
    n = len(messages[0])
    columns = ['' for i in range(n)]
    for message in messages:
        for i in range(n):
            columns[i] += message[i]
    return [countLetter(columns[i]) for i in range(n)]

# Return a list of the most common letter for each string
def findMostCommonLetter(letterCount):
    for i in range(len(letterCount)):
        letterCount[i].sort(key=lambda x: x[0])
        letterCount[i].sort(key=lambda x: x[1], reverse=True)
        print(letterCount)
    return [letterCount[i][0] for i in range(len(letterCount))]

# Return a list of the less common letter for each string
def findLessCommonLetter(letterCount):
    for i in range(len(letterCount)):
        letterCount[i].sort(key=lambda x: x[0])
        letterCount[i].sort(key=lambda x: x[1], reverse=True)
        print(letterCount)
    return [letterCount[i][-1] for i in range(len(letterCount))]

# Return the first answer
def answer():
    messages = readMessageFromFile("D:/Perso/Programmation/Python/AdventOfCode/Day6/message.txt")
    letterCount = getFrequencyFromMessages(messages)
    return findMostCommonLetter(letterCount)

# Return the second answer
def answer2():
    messages = readMessageFromFile("D:/Perso/Programmation/Python/AdventOfCode/Day6/message.txt")
    letterCount = getFrequencyFromMessages(messages)
    return findLessCommonLetter(letterCount)

print(answer2())