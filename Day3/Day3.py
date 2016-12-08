from math import *

# Check if a triangle is possible
def checkTriangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False

# Return the list of all the triangles in the file
def getTrianglesFromFile(filename):
    triangles = []
    file = open(filename, 'r')
    for line in file:
        splittedLine = line.split()
        triangles.append(splittedLine)
    return triangles

# Return the list of triangles side length read by group of 3 vertically
def getTriangleVerticallyFromFile(filename):
    lengthLine = []
    triangles = []
    file = open(filename, 'r')
    for line in file:
        splittedLine = line.split()
        lengthLine.append(splittedLine)
    for i in range(0, len(lengthLine), 3):
        triangles.append([lengthLine[i][0], lengthLine[i + 1][0], lengthLine[i + 2][0]])
        triangles.append([lengthLine[i][1], lengthLine[i + 1][1], lengthLine[i + 2][1]])
        triangles.append([lengthLine[i][2], lengthLine[i + 1][2], lengthLine[i + 2][2]])
    return triangles

# Return the first answer
def answer():
    triangles = getTrianglesFromFile("D:/Perso/Programmation/Python/AdventOfCode/Day3/triangle.txt")
    count = 0
    for triangle in triangles:
        if checkTriangle(int(triangle[0]), int(triangle[1]), int(triangle[2])):
            count += 1
    return count

# Return the second answer
def answer2():
    triangles = getTriangleVerticallyFromFile("D:/Perso/Programmation/Python/AdventOfCode/Day3/triangle.txt")
    count = 0
    for triangle in triangles:
        if checkTriangle(int(triangle[0]), int(triangle[1]), int(triangle[2])):
            count += 1
    return count

print(answer2())
