from math import *

path = 'R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5'
path2 = 'R5, L5, R5, R3'
path3 = 'R8, R4, R4, R8'
#    +
#    ^
#    |
#    |
#    |
#    +---------> +


# Return a list of instructions from the path
def getInstructionsFromPath(path):
    return path.split(', ')

# Return the new position and orientation after all the instructions
def computeNewPositionFromInstructions(instructions, startingPositionAndOrientation):
    finalPosition = startingPositionAndOrientation
    for inst in instructions:
        finalPosition = applyInstruction(inst, finalPosition)
    return finalPosition

# Return the new orientation
def computeNewOrientation(currentOrientation, rotation):
    if rotation == 'R':
        if currentOrientation == 'N':
            return 'E'
        elif currentOrientation == 'E':
            return 'S'
        elif currentOrientation == 'S':
            return 'W'
        elif currentOrientation == 'W':
            return 'N'
    elif rotation == 'L':
        if currentOrientation == 'N':
            return 'W'
        elif currentOrientation == 'E':
            return 'N'
        elif currentOrientation == 'S':
            return 'E'
        elif currentOrientation == 'W':
            return 'S'
    return None

# Return the new position
def computeNewPosition(currentPosition, distance, newOrientation):
    x, y = currentPosition
    if newOrientation == 'N':
        y += distance
    elif newOrientation == 'W':
        x -= distance
    elif newOrientation == 'S':
        y -= distance
    elif newOrientation == 'E':
        x += distance
    return (x, y)

# Return the new position and all the position visited in the process
def computeNewPositionAndIntermediatePosition(currentPosition, distance, newOrientation):
    x, y = currentPosition
    intermediatePosition = []
    i = 1
    if newOrientation == 'N':
        while(i <= distance):
            y += 1
            intermediatePosition.append((x, y))
            i += 1
    elif newOrientation == 'W':
        while (i <= distance):
            x -= 1
            intermediatePosition.append((x, y))
            i += 1
    elif newOrientation == 'S':
        while (i <= distance):
            y -= 1
            intermediatePosition.append((x, y))
            i += 1
    elif newOrientation == 'E':
        while (i <= distance):
            x += 1
            intermediatePosition.append((x, y))
            i += 1
    return (x, y), intermediatePosition

# Return the new position and orientation after one instruction
def applyInstruction(instruction, positionAndOrientation):
    rotation = instruction[0]
    distance = int(instruction[1:])
    newOrientation = computeNewOrientation(positionAndOrientation[1], rotation)
    newPosition = computeNewPosition(positionAndOrientation[0], distance, newOrientation)
    return newPosition, newOrientation

# Return the new position and orientation after one instruction and all the position visited
def applyInstructionAndGiveIntermediatePosition(instruction, positionAndOrientation):
    rotation = instruction[0]
    distance = int(instruction[1:])
    newOrientation = computeNewOrientation(positionAndOrientation[1], rotation)
    newPosition, intermediatePosition = computeNewPositionAndIntermediatePosition(positionAndOrientation[0], distance, newOrientation)
    return (newPosition, newOrientation), intermediatePosition

# Return the TaxiCab distance between the 2 points
def computeTaxiCabDistance(startingPosition, endingPosition):
    return abs(endingPosition[0][0] - startingPosition[0][0]) + abs(endingPosition[0][1] - startingPosition[0][1])

# Return the first place visited twice or None if there is none
def findFirstPlaceVisitedTwice(instructions, startingPositionAndOrientation):
    visitedPlace = [startingPositionAndOrientation[0]]
    finalPosition = startingPositionAndOrientation
    for inst in instructions:
        finalPosition, intermediate = applyInstructionAndGiveIntermediatePosition(inst, finalPosition)
        for pos in intermediate:
            print(pos)
            if pos in visitedPlace:
                return pos, 'N'
            else:
                visitedPlace.append(pos)
    return None

def answer(path):
    instructions = getInstructionsFromPath(path)
    startingPositionAndOrientation = ((0, 0), 'N')
    finalPositionAndOrientation = computeNewPositionFromInstructions(instructions, startingPositionAndOrientation)
    return computeTaxiCabDistance(startingPositionAndOrientation, finalPositionAndOrientation)

def answer2(path):
    instructions = getInstructionsFromPath(path)
    startingPositionAndOrientation = ((0, 0), 'N')
    finalPositionAndOrientation = findFirstPlaceVisitedTwice(instructions, startingPositionAndOrientation)
    return computeTaxiCabDistance(startingPositionAndOrientation, finalPositionAndOrientation)

print(answer2(path))