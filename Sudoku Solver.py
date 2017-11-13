from copy import deepcopy
from tkinter import *
from vars import *
from pprint import pprint
master = Tk()
c = Canvas(master, height=HEIGHT, width=WIDTH)
c.pack()

Sdk = deepcopy(OSdk)


def drawGrid():
    for i in range(8):
        w = 1
        if i == 2 or i == 5:
            w = 3
        c.create_line(0, (i + 1) * 50, WIDTH, (i + 1) * 50, fill="black", width=w)
        c.create_line((i + 1) * 50, 0, (i + 1) * 50, HEIGHT, fill="black", width=w)


def drawNum():
    for y in range(9):
        for x in range(9):
            if Sdk[y][x] != 0:
                if Sdk[y][x] == OSdk[y][x]:
                    c.create_text(x * 50 + 25, y * 50 + 25, font=("Arial", 20), text=Sdk[y][x], fill="red")
                else:
                    c.create_text(x * 50 + 25, y * 50 + 25, font=("Arial", 20), text=Sdk[y][x], fill="black")


def draw():
    c.delete("all")
    drawGrid()
    drawNum()


def checkRow(n, _x, y):
    for x in range(9):
        if n == Sdk[y][x] and x != _x:
            return False
    return True


def checkCol(n, x, _y):
    for y in range(9):
        if n == Sdk[y][x] and y != _y:
            return False
    return True


def checkSq(n, x, y):
    minX = int(x / 3) * 3
    minY = int(y / 3) * 3

    maxX = (int(x / 3) + 1) * 3
    maxY = (int(y / 3) + 1) * 3

    for y in range(minY, maxY):
        for x in range(minX, maxX):
            if n == Sdk[y][x]:
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
            if Sdk[y][x] == 0:
                nums[y][x] = getEMN(x, y)
    return nums


def setNums():
    nums = checkEN()
    for y in range(9):
        for x in range(9):
            if len(nums[y][x]) == 1 and nums[y][x][0] != 0:
                n = nums[y][x][0]
                Sdk[y][x] = n

def solveSudoku():
    solved = False
    while not solved:
        setNums()
        for y in range(9):
            for x in range(9):
                if Sdk[y][x] == 0:
                    solved = False
                    break
                elif x == 8 and y == 8 and Sdk[y][x] != 0:
                    solved = True

def my_mainloop():
    solveSudoku()

    draw()

master.after(40, my_mainloop)
master.mainloop()

# TODO resolve the x y / y x  problem
# TODO add a better mode to change the numbers
# TODO add some button or thing to solve the sudoku
# TODO add a menu !
