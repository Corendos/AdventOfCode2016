
# Return a list of alla instructions contained in the input file
def readInstructionsFromFile(filename):
    f = open(filename, 'r')

    instructions = []

    for line in f:
        instructions.append(line[:len(line) - 1])
    return instructions

# Decode an instruction and return a list of parameters it contains
def decodeInstruction(instruction):
    return instruction.split(' ')

# Return a screen of size width*height
def initScreen(width, height):
    return [[' ' for i in range(width)] for j in range(height)]

# Return the screen after creating a rectangle starting in the top left corner with a size of width*height
def rectInstruction(width, height, screen):
    screenWidth = len(screen[0])
    screenHeight = len(screen)
    for i in range(min(height, screenHeight)):
        for j in range(min(width, screenWidth)):
            screen[i][j] = '#'
    return screen

# Return the screen after applying the rotation
def rotateInstruction(mode, index, shift, screen):
    screenWidth = len(screen[0])
    screenHeight = len(screen)
    replacment = []
    if mode == 'row':
        for i in range(screenWidth):
            replacment.append(screen[index][(i - shift)%screenWidth])
        for i in range(screenWidth):
            screen[index][i] = replacment[i]
        return screen
    elif mode == 'column':
        for i in range(screenHeight):
            replacment.append(screen[(i - shift)%screenHeight][index])
        for i in range(screenHeight):
            screen[i][index] = replacment[i]
        return screen
    else:
        return

# Print the screen
def printScreen(screen):
    print("Screen:")
    for i in range(len(screen)):
        print(''.join(screen[i]))

# Return the screen after applying a series of instructions
def applyInstructions(instructions, screen):
    for instruction in instructions:
        decodedInstruction = decodeInstruction(instruction)
        if decodedInstruction[0] == 'rect':
            width, height = decodedInstruction[1].split('x')
            screen = rectInstruction(int(width), int(height), screen)
        elif decodedInstruction[0] == 'rotate':
            mode = decodedInstruction[1]
            index = decodedInstruction[2].split('=')[1]
            shift = decodedInstruction[4]
            screen = rotateInstruction(mode, int(index), int(shift), screen)
        printScreen(screen)
    return screen

# Return the number of lit pixels
def countLitPixels(screen):
    countLit = 0
    countOff = 0
    width = len(screen[0])
    height = len(screen)
    for i in range(height):
        for j in range(width):
            if screen[i][j] == '#':
                countLit += 1
            elif screen[i][j] == ' ':
                countOff += 1
    return countLit, countOff

def answer():
    instructions = readInstructionsFromFile('D:/Perso/Programmation/Python/AdventOfCode/Day8/card_instructions.txt')
    screen = initScreen(50, 6)
    screen = applyInstructions(instructions, screen)
    printScreen(screen)
    return countLitPixels(screen)

print(answer())