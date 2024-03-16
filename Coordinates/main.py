import tkinter as tk
from random import randint

WIDTH = HEIGHT = 600
HALF_WIDTH = HALF_HEIGHT = 600//2
canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()

def axes():
    coordinates = [((WIDTH-20, HALF_HEIGHT-10), (WIDTH-20, HALF_HEIGHT+10), (WIDTH, HALF_HEIGHT)), ((25, HALF_HEIGHT-10), (25, HALF_HEIGHT+10), (5, HALF_HEIGHT)), 
                   ((HALF_WIDTH-10, 25), (HALF_WIDTH+10, 25), (HALF_WIDTH, 5)), ((HALF_WIDTH-10, HEIGHT-20), (HALF_WIDTH+10, HEIGHT-20), (HALF_WIDTH, HEIGHT))]
    for coords in coordinates:
        canvas.create_polygon(*coords)

    canvas.create_line(20, HALF_HEIGHT, WIDTH-10, HALF_HEIGHT)
    canvas.create_line(HALF_WIDTH, 20, HALF_WIDTH, HEIGHT-10)

    canvas.create_text(HALF_WIDTH + 17, HALF_HEIGHT + 25, text=0)
    canvas.create_text(WIDTH - 20, HALF_HEIGHT + 50, text='x')
    canvas.create_text(HALF_WIDTH + 30, 20, text='y')

    for i in range(1, WIDTH//40):
        canvas.create_text(HALF_WIDTH - 25, HALF_HEIGHT + (40*i), text=-20*i)
        canvas.create_text(HALF_WIDTH - 25, HALF_HEIGHT - (40*i), text=20*i)
        canvas.create_text(HALF_WIDTH + (40*i), HALF_HEIGHT + 25, text=20*i)
        canvas.create_text(HALF_WIDTH - (40*i), HALF_HEIGHT + 25, text=-20*i)

        canvas.create_line(HALF_WIDTH-5, HALF_HEIGHT - 40*i, HALF_WIDTH+5, HALF_HEIGHT - 40*i)
        canvas.create_line(HALF_WIDTH-5, HALF_HEIGHT + 40*i, HALF_WIDTH+5, HALF_HEIGHT + 40*i)
        canvas.create_line(HALF_WIDTH + 40*i, HALF_HEIGHT - 5, HALF_WIDTH + 40*i, HALF_HEIGHT + 5)
        canvas.create_line(HALF_WIDTH - 40*i, HALF_HEIGHT - 5, HALF_WIDTH - 40*i, HALF_HEIGHT + 5)


def assign_quadrant(n1, n2):
    if n1 > HALF_WIDTH-5:
        if n2 <= HALF_HEIGHT:
            return 1
        return 4
    else:
        if n2 <= HALF_HEIGHT-5:
            return 2
        return 3
 

def points(n, size=10):
    colours = ['red', 'orange', 'blue', 'green']

    for i in range(n):
        random_x, random_y = randint(0 + size, WIDTH - size), randint(0 + size, HEIGHT - size)
        colour = colours[assign_quadrant(random_x, random_y)-1]
        canvas.create_oval(random_x, random_y, random_x + size, random_y + size, fill=colour, outline=colour)


axes()
points(300)

tk.mainloop()
