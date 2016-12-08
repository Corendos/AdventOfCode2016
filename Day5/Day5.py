from hashlib import *

# Return the hash from the string
def computeHash(string):
    return md5(string.encode('utf-8')).hexdigest()

# Check if the hash starts with 5 '0'
def checkMD5(string):
    hashed = str(computeHash(string))
    if hashed[0:5] == '00000':
        return True, hashed[5], hashed[6]
    return False, None, None

# Return the first answer
def answer(doorID):
    code = [None] * 8
    i = 0
    while None in code:
        res, pos, c = checkMD5(doorID + str(i))
        if res:
            if pos in ['0', '1', '2', '3', '4', '5', '6', '7']:
                pos = int(pos)
                if pos in range(0, 8) and code[pos] == None:
                    code[pos] = c
                    print(code)
        i += 1
    return code

print(answer('ffykfhsq'))