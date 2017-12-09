from tkinter import *
import vars as v
from Algorithm import solveSudoku

v.init()

master = Tk()
c = Canvas(master, height=v.HEIGHT, width=v.WIDTH)

c.pack()


def drawGrid():
    for i in range(8):
        w = 1
        if i == 2 or i == 5:
            w = 3
        c.create_line(0, (i + 1) * 50, v.WIDTH, (i + 1) * 50, fill="black", width=w)
        c.create_line((i + 1) * 50, 0, (i + 1) * 50, v.HEIGHT, fill="black", width=w)


def drawNum():
    for y in range(9):
        for x in range(9):
            if v.Sdk[y][x] != 0:
                if v.Sdk[y][x] == v.OSdk[y][x]:
                    c.create_text(x * 50 + 25, y * 50 + 25, font=("Arial", 20), text=v.Sdk[y][x], fill="red")
                else:
                    c.create_text(x * 50 + 25, y * 50 + 25, font=("Arial", 20), text=v.Sdk[y][x], fill="black")


def draw():
    c.delete("all")
    drawGrid()
    drawNum()

def solve():
    solveSudoku()

def my_mainloop():
    solveSudoku()
    draw()

master.after(40, my_mainloop)
master.mainloop()

# TODO add a better mode to change the numbers
# TODO add some button or thing to solve the sudoku
# TODO add a menu !
