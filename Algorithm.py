import vars as v
from copy import deepcopy

sdk = [[]]

def checkRow(n, _x, y):
    for x in range(9):
        if n == sdk[y][x] and x != _x:
            return False
    return True

def checkCol(n, x, _y):
    for y in range(9):
        if n == sdk[y][x] and y != _y:
            return False
    return True


def checkSq(n, x, y):
    minX = int(x / 3) * 3
    minY = int(y / 3) * 3

    maxX = (int(x / 3) + 1) * 3
    maxY = (int(y / 3) + 1) * 3

    for y in range(minY, maxY):
        for x in range(minX, maxX):
            if n == sdk[y][x]:
                return False
    return True


def check(n, x, y):
    if checkRow(n, x, y) and checkCol(n, x, y) and checkSq(n, x, y):
        return True
    return False


def getEMN(x, y):  # getEveryMatchingNumber
    nms = []
    for n in range(1, 10):
        if check(n, x, y):
            nms.append(n)
    return nms


def checkEN():
    nums = [[[0] for j in range(9)] for i in range(9)]
    for y in range(9):
        for x in range(9):
            if sdk[y][x] == 0:
                nums[y][x] = getEMN(x, y)
    return nums


def setNums():
    nums = checkEN()
    for y in range(9):
        for x in range(9):
            if len(nums[y][x]) == 1 and nums[y][x][0] != 0:
                n = nums[y][x][0]
                sdk[y][x] = n


def solveSudoku(OSdk):
    global sdk
    sdk = deepcopy(OSdk)

    solved = False
    while not solved:
        setNums()
        br = False
        for y in range(9):
            for x in range(9):
                solved = True
                if sdk[y][x] == 0:  # and v.OSdk[y][x] != sdk[y][x]:
                    solved = False
                    br = True
                    break
            if br:
                break

    return sdk
