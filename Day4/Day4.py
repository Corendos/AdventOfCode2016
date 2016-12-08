
# Return a list of room name from the file
def getRoomsFromFile(filename):
    file = open(filename, 'r')
    rooms = []
    for line in file:
        rooms.append(line[:len(line) - 1])
    return rooms

# Return the ID and the checksum from a string in this shape: 645[azeez]
def divideChecksum(IDChecksum):
    ID = ''
    Checksum = ''
    opened = False
    for c in IDChecksum:
        if c == '[':
            opened = True
        elif c == ']':
            opened = False
        elif not opened:
            ID += c
        elif opened:
            Checksum += c
    return ID, Checksum

# Count the frequency of each letter
def countLetter(str):
    L = [(chr(i), 0) for i in range(97, 97 + 26)]
    for c in str:
        L[ord(c) - 97] = (L[ord(c) - 97][0],L[ord(c) - 97][1] + 1)
    return L

# Return whether or not a checksum is valid
def validChecksum(mostCommonLetters, wantedCommonLetters):
    if len(mostCommonLetters) == len(wantedCommonLetters):
        valid = True
        for c in mostCommonLetters:
            if c not in wantedCommonLetters:
                valid = False
        return valid
    return False

# Check if a room is valid
def checkRoom(roomName):
    splittedName = roomName.split('-')
    letter = ''.join(splittedName[:len(splittedName) - 1])
    IDChecksum = splittedName[-1]
    ID, Checksum = divideChecksum(IDChecksum)
    frequency = countLetter(letter)
    frequency.sort(key=lambda x: x[0])
    frequency.sort(key=lambda x: x[1], reverse=True)
    print(frequency)
    mostCommonLetter = ''.join([frequency[i][0] for i in range(5)])
    return validChecksum(mostCommonLetter, Checksum), ID

# Return the first answer
def answer():
    rooms = getRoomsFromFile("D:/Perso/Programmation/Python/AdventOfCode/Day4/room.txt")
    totalChecksum = 0
    for room in rooms:
        result, checksum = checkRoom(room)
        if result:
            totalChecksum += int(checksum)
    return totalChecksum

# Return the decyphered room name
def decypherRoom(room):
    splittedName = room.split('-')
    letter = ''.join(splittedName[:len(splittedName) - 1])
    IDChecksum = splittedName[-1]
    ID, Checksum = divideChecksum(IDChecksum)

    ID = int(ID)
    for i in range(len(splittedName) - 1):
        data = splittedName[i]
        str = ''
        for c in data:
            d = ord(c) - ord('a')
            d += ID
            newC = chr((d % 26) + ord('a'))
            str += newC
        splittedName[i] = str
    return '-'.join(splittedName)

# Return the second answer
def answer2():
    rooms = getRoomsFromFile("D:/Perso/Programmation/Python/AdventOfCode/Day4/room.txt")
    decypheredRooms = []
    for room in rooms:
        decypheredRooms.append(decypherRoom(room))
    return decypheredRooms

print(answer2())