from tkinter import *
import vars as v
from Algorithm import solveSudoku

master = Tk()
c = Canvas(master, height=v.WINDOW_HEIGHT, width=v.WINDOW_WIDTH)

c.pack()

class Number:
    n = 0
    x = 0
    y = 0

    def __init__(self, n_, x_, y_):
        self.n = n_
        self.x = x_
        self.y = y_

def drawGrid():
    for i in range(8):
        w = 1
        if i == 2 or i == 5:
            w = 3
        c.create_line(0, (i + 1) * 50, v.GRID_WIDTH, (i + 1) * 50, fill="black", width=w)
        c.create_line((i + 1) * 50, 0, (i + 1) * 50, v.GRID_HEIGHT, fill="black", width=w)

    c.create_line(v.GRID_WIDTH, 0, v.GRID_WIDTH, v.GRID_HEIGHT, fill="black", width=3)
    c.create_line(3, 0, 3, v.GRID_HEIGHT, fill="black", width=3)
    c.create_line(0, 3, v.GRID_WIDTH, 3, fill="black", width=3)
    c.create_line(0, v.GRID_HEIGHT, v.GRID_WIDTH, v.GRID_HEIGHT, fill="black", width=3)

def createNums():
    for y in range(9):
        for x in range(9):
            v.Sdk[y][x] = Number(v.OSdk[y][x], x * 50 + 25, y * 50 + 25)
            #print(v.Sdk[y][x].n)



def drawNums(num,x,y):
    for y in range(9):
        for x in range(9):
            if v.Sdk[y][x].n != 0:
                if v.Sdk[y][x].n == v.OSdk[y][x]:
                    c.create_text(v.Sdk[y][x].x, v.Sdk[y][x].y, font=("Arial", 20), text=v.Sdk[y][x].n, fill="red")
                else:
                    c.create_text(v.Sdk[y][x].x, v.Sdk[y][x].y, font=("Arial", 20), text=v.Sdk[y][x].n, fill="black")


def solve():
    solveSudoku(v.OSdk)

createNums()

def draw():
    c.delete("all")
    drawGrid()
    #drawNums()

def my_mainloop():
    print(v.Sdk[0][0].n)
    v.Sdk = solveSudoku(v.OSdk)
    print(v.Sdk[0][0].n)
    draw()

master.after(40, my_mainloop)
master.mainloop()

# TODO add a better mode to change the numbers
# TODO add some button or thing to solve the sudoku
# TODO add a menu !
