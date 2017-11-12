from tkinter import *
from vars import *
from copy import deepcopy

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
    # c.delete("all")
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


def nums():
    for y in range(9):
        for x in range(9):
            for n in range(1, 10):
                if OSdk[y][x] == 0 and check(n, x, y):
                    Sdk[y][x] = n
                    break

whiteSp = []
def backtrack():
    for y in range(9):
        for x in range(9):
            if Sdk[y][x] == 0:
                whiteSp.append((y,x))
                c.create_oval(x * 50 + 2, y * 50 + 2, x * 50 + 48, y * 50 + 48)

    while len(whiteSp) != 0:
        for idx in range(len(whiteSp)):
            x = whiteSp[idx][0]
            y = whiteSp[idx][1]
            rowN = []
            colN = []
            sqN = []

            for n in range(9):
                if checkRow(n, x, y):
                    rowN.append(n)

                if checkCol(n, x, y):
                    colN.append(n)

                if checkSq(n, x, y):
                    sqN.append(n)

            while True:
                iRow = 0
                iCol = 0
                iSq = 0

                # TODO find a way to itterate through all possible combinations

                if rowN[iRow] == colN[iCol] and colN[iCol] == sqN[iSq]:
                    Sdk[x][y] = n


                break



nums()
backtrack()
print(whiteSp)

# def my_mainloop():
draw()

# master.after(40, my_mainloop)
master.mainloop()

#TODO resolve the x y / y x  problem
#TODO add a better mode to change the numbers
#TODO add some button or thing to solve the sudoku
#TODO add a menu !

