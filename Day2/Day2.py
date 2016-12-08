from math import *

code = 'RDLULDLDDRLLLRLRULDRLDDRRRRURLRLDLULDLDLDRULDDLLDRDRUDLLDDRDULLLULLDULRRLDURULDRUULLLUUDURURRDDLDLDRRDDLRURLLDRRRDULDRULURURURURLLRRLUDULDRULLDURRRLLDURDRRUUURDRLLDRURULRUDULRRRRRDLRLLDRRRDLDUUDDDUDLDRUURRLLUDUDDRRLRRDRUUDUUULDUUDLRDLDLLDLLLLRRURDLDUURRLLDLDLLRLLRULDDRLDLUDLDDLRDRRDLULRLLLRUDDURLDLLULRDUUDRRLDUDUDLUURDURRDDLLDRRRLUDULDULDDLLULDDDRRLLDURURURUUURRURRUUDUUURULDLRULRURDLDRDDULDDULLURDDUDDRDRRULRUURRDDRLLUURDRDDRUDLUUDURRRLLRR\nRDRRLURDDDDLDUDLDRURRLDLLLDDLURLLRULLULUUURLDURURULDLURRLRULDDUULULLLRLLRDRRUUDLUUDDUDDDRDURLUDDRULRULDDDLULRDDURRUURLRRLRULLURRDURRRURLDULULURULRRLRLUURRRUDDLURRDDUUDRDLLDRLRURUDLDLLLLDLRURDLLRDDUDDLDLDRRDLRDRDLRRRRUDUUDDRDLULUDLUURLDUDRRRRRLUUUDRRDLULLRRLRLDDDLLDLLRDDUUUUDDULUDDDUULDDUUDURRDLURLLRUUUUDUDRLDDDURDRLDRLRDRULRRDDDRDRRRLRDULUUULDLDDDUURRURLDLDLLDLUDDLDLRUDRLRLDURUDDURLDRDDLLDDLDRURRULLURULUUUUDLRLUUUDLDRUDURLRULLRLLUUULURLLLDULLUDLLRULRRLURRRRLRDRRLLULLLDURDLLDLUDLDUDURLURDLUURRRLRLLDRLDLDRLRUUUDRLRUDUUUR\nLLLLULRDUUDUUDRDUUURDLLRRLUDDDRLDUUDDURLDUDULDRRRDDLLLRDDUDDLLLRRLURDULRUUDDRRDLRLRUUULDDULDUUUDDLLDDDDDURLDRLDDDDRRDURRDRRRUUDUUDRLRRRUURUDURLRLDURDDDUDDUDDDUUDRUDULDDRDLULRURDUUDLRRDDRRDLRDLRDLULRLLRLRLDLRULDDDDRLDUURLUUDLLRRLLLUUULURUUDULRRRULURUURLDLLRURUUDUDLLUDLDRLLRRUUDDRLUDUDRDDRRDDDURDRUDLLDLUUDRURDLLULLLLUDLRRRUULLRRDDUDDDUDDRDRRULURRUUDLUDLDRLLLLDLUULLULLDDUDLULRDRLDRDLUDUDRRRRLRDLLLDURLULUDDRURRDRUDLLDRURRUUDDDRDUUULDURRULDLLDLDLRDUDURRRRDLDRRLUDURLUDRRLUDDLLDUULLDURRLRDRLURURLUUURRLUDRRLLULUULUDRUDRDLUL\nLRUULRRUDUDDLRRDURRUURDURURLULRDUUDUDLDRRULURUDURURDRLDDLRUURLLRDLURRULRRRUDULRRULDLUULDULLULLDUDLLUUULDLRDRRLUURURLLUUUDDLLURDUDURULRDLDUULDDRULLUUUURDDRUURDDDRUUUDRUULDLLULDLURLRRLRULRLDLDURLRLDLRRRUURLUUDULLLRRURRRLRULLRLUUDULDULRDDRDRRURDDRRLULRDURDDDDDLLRRDLLUUURUULUDLLDDULDUDUUDDRURDDURDDRLURUDRDRRULLLURLUULRLUDUDDUUULDRRRRDLRLDLLDRRDUDUUURLRURDDDRURRUDRUURUUDLRDDDLUDLRUURULRRLDDULRULDRLRLLDRLURRUUDRRRLRDDRLDDLLURLLUDL\nULURLRDLRUDLLDUDDRUUULULUDDDDDRRDRULUDRRUDLRRRLUDLRUULRDDRRLRUDLUDULRULLUURLLRLLLLDRDUURDUUULLRULUUUDRDRDRUULURDULDLRRULUURURDULULDRRURDLRUDLULULULUDLLUURULDLLLRDUDDRRLULUDDRLLLRURDDLDLRLLLRDLDRRUUULRLRDDDDRUDRUULDDRRULLDRRLDDRRUDRLLDUDRRUDDRDLRUDDRDDDRLLRDUULRDRLDUDRLDDLLDDDUUDDRULLDLLDRDRRUDDUUURLLUURDLULUDRUUUDURURLRRDULLDRDDRLRDULRDRURRUDLDDRRRLUDRLRRRRLLDDLLRLDUDUDDRRRUULDRURDLLDLUULDLDLDUUDDULUDUDRRDRLDRDURDUULDURDRRDRRLLRLDLU'
code2 = 'ULL\nRRDDD\nLURDL\nUUUUD'
# Return instructions from the code
def getInstructionsFromCode(code):
    return code.split('\n')

# Return the clamped value
def clamp(x, a, b):
    if x > b:
        return b
    elif x < a:
        return a
    else:
        return x

# Return the new position after one instruction
def applyInstruction(instruction, currentPos):
    x, y = currentPos
    if instruction == 'R':
        x += 1
    elif instruction == 'L':
        x -= 1
    elif instruction == 'D':
        y += 1
    elif instruction == 'U':
        y -= 1

    return clamp(x, 0, 2), clamp(y, 0, 2)

# Return the final position after every instructions in the line
def applyInstructions(instructions, startingPosition):
    finalPosition = startingPosition
    for inst in instructions:
        finalPosition = applyInstruction(inst, finalPosition)
    return finalPosition

def findCombination(code):
    instructionsSequence = getInstructionsFromCode(code)
    lastButton = (1, 1)
    sequence = []
    for instructions in instructionsSequence:
        lastButton = applyInstructions(instructions, lastButton)
        sequence.append(3 * lastButton[1] + lastButton[0] + 1)
    return sequence

# Return the manhattan distance from the center
def distanceFromCenter(position):
    x, y = position
    return abs(x) + abs(y)

# Return the position where we can go from the current position
def findPossibleDestinationFromPosition(currentPosition):
    x, y = currentPosition
    destination = []
    if distanceFromCenter((x + 1, y)) <= 2:
        destination.append('R')
    if distanceFromCenter((x - 1, y)) <= 2:
        destination.append('L')
    if distanceFromCenter((x, y + 1)) <= 2:
        destination.append('D')
    if distanceFromCenter((x, y - 1)) <= 2:
        destination.append('U')
    return destination

# Return the new position after one instruction on the weird keypad
def applyInstructionOnWeirdKeypad(instruction, currentPos):
    x, y = currentPos
    possibleDestination = findPossibleDestinationFromPosition(currentPos)
    if instruction in possibleDestination:
        if instruction == 'R':
            x += 1
        elif instruction == 'L':
            x -= 1
        elif instruction == 'D':
            y += 1
        elif instruction == 'U':
            y -= 1

    return x, y

# Return the final position after every instructions in the line on the weird keypad
def applyInstructionsOnWeirdKeypad(instructions, startingPosition):
    finalPosition = startingPosition
    for inst in instructions:
        finalPosition = applyInstructionOnWeirdKeypad(inst, finalPosition)
    return finalPosition

def findCombination2(code):
    instructionsSequence = getInstructionsFromCode(code)
    lastButton = (-2, 0)
    sequence = []

    keypad = {(-2,0):'5',
              (-1,0):'6',
              (0,0):'7',
              (1,0):'8',
              (2,0):'9',
              (-1,1):'A',
              (0,1):'B',
              (1,1):'C',
              (0,2):'D',
              (-1,-1):'2',
              (0,-1):'3',
              (1,-1):'4',
              (0,-2):'1'}

    for instructions in instructionsSequence:
        lastButton = applyInstructionsOnWeirdKeypad(instructions, lastButton)

        sequence.append(keypad[lastButton])
    return sequence

print(findCombination2(code))