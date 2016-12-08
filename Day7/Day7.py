# Return the list of each IP in the input file
def readMessageFromFile(filename):
    messages = []
    f = open(filename, 'r')
    for line in f:
        messages.append(line[:len(line) - 1])
    return messages

def retrievePartsOfIP(ip):
    outsideBracket = []
    insideBracket = []
    opened = False
    currentString = ''
    for c in ip:
        if c == '[':
            opened = True
            outsideBracket.append(currentString)
            currentString = ''
        elif c == ']':
            opened = False
            insideBracket.append(currentString)
            currentString = ''
        else:
            currentString += c
    outsideBracket.append(currentString)
    return outsideBracket, insideBracket

def isABBA(sequence):
    a = sequence[0]
    b = sequence[1]
    if a == b:
        return False
    if a == sequence[3] and b == sequence[2]:
        return True
    return False

def sequenceContainsABBA(sequences):
    res = True
    for sequence in sequences:
        if not containsABBA(sequence):
            res = False
    return res

def containsOneABBA(sequences):
    res = False
    for sequence in sequences:
        if containsABBA(sequence):
            res = True
    return res

def containsABBA(sequence):
    res = False
    for i in range(0, len(sequence) - 3):
        if isABBA(sequence[i:i+4]):
            res = True
    return res

def supportTLS(ip):
    outside, inside = retrievePartsOfIP(ip)
    return containsOneABBA(outside) and not containsOneABBA(inside)

def answer():
    sequences = readMessageFromFile('D:/Perso/Programmation/Python/AdventOfCode/Day7/IP.txt')
    count = 0
    for sequence in sequences:
        if supportTLS(sequence):
            print(sequence)
            count += 1
    return count

# Return whether or not a string is an ABA
def isABA(potentialABA):
    if(potentialABA[0] == potentialABA[1]):
        return False
    else:
        return potentialABA[2] == potentialABA[0]

# Return all the ABAs in an IPv7 adress
def findABAInIp(ipPart):
    res = False
    ABAs = []
    for i in range(0, len(ipPart) - 2):
        if isABA(ipPart[i:i + 3]):
            res = True
            ABAs.append(ipPart[i:i + 3])
    return res, ABAs

# Return all the ABAs in a sequence of IP part
def findABAinSequences(sequences):
    ABAs = []
    for ipPart in sequences:
        res, ABA = findABAInIp(ipPart)
        if res:
            ABAs += ABA
    return ABAs

# Return the reversed ABAs
def reverseABAs(ABAs):
    BABs = []
    for ABA in ABAs:
        BABs.append(ABA[1] + ABA[0] + ABA[1])
    return BABs

# Return True if an ip supports SSL
def supportSSL(ip):
    outside, inside = retrievePartsOfIP(ip)
    outsideABAs = findABAinSequences(outside)
    reversedOutsideABAs = set(reverseABAs(outsideABAs))
    insideBABs = set(findABAinSequences(inside))
    return len(reversedOutsideABAs.intersection(insideBABs)) != 0

def answer2():
    ips = readMessageFromFile('D:/Perso/Programmation/Python/AdventOfCode/Day7/IP.txt')
    count = 0
    for ip in ips:
        if supportSSL(ip):
            count += 1
    return count

print(answer2())