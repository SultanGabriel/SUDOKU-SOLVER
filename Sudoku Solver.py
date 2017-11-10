from tkinter import *
from vars import *
from copy import deepcopy

master = Tk()
c = Canvas(master, height=HEIGHT, width=WIDTH)
c.pack()

Sdk = deepcopy(OSdk)


def drawGrid():
    for i in range(8):
        c.create_line(0, (i + 1) * 50, WIDTH, (i + 1) * 50, fill="black")
        c.create_line((i + 1) * 50, 0, (i + 1) * 50, HEIGHT, fill="black")


def drawNum():
    for i in range(9):
        for j in range(9):
            if Sdk[i][j] != 0:
                if Sdk[i][j] == OSdk[i][j]:
                    c.create_text(j * 50 + 25, i * 50 + 25, font=("Arial", 20), text=Sdk[i][j], fill="red")
                else:
                    c.create_text(j * 50 + 25, i * 50 + 25, font=("Arial", 20), text=Sdk[i][j], fill="black")


def draw():
    c.delete("all")
    drawNum()
    drawGrid()


def checkRow(n, j):
    for x in range(9):
        if n == Sdk[j][x]:
            return False
    return True


def checkCol(n, i):
    for x in range(9):
        if n == Sdk[x][i]:
            return False
    return True


def checkSq(n, i, j):
    if int(j / 3) == 0:
        if int(i / 3) == 0:
            for x in range(3):
                for y in range(3):
                    if n == Sdk[y][x]:
                        return False
            return True

        if int(i / 3) == 1:
            for x in range(3):
                for y in range(3, 6):
                    print(y,x)
                    if n == Sdk[y][x]:
                        return False
            return True

        if int(i / 3) == 2:
            for x in range(3):
                for y in range(6, 9):
                    print(x,y)
                    if n == Sdk[y][x]:
                        return False
            return True


print(checkSq(7,3,0))


def my_mainloop():
    draw()


master.after(40, my_mainloop)
master.mainloop()
