import tkinter as tk
from random import randint, choice

WIDTH, HEIGHT = 800, 600
canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bg="#1f1f1f")
canvas.pack()


def constellation(cons_cord):
    [canvas.create_line(cons_cord[i][0] + 5, cons_cord[i][1] + 5, cons_cord[i+1][0] + 5, cons_cord[i+1][1] + 5, 
                        fill="white", width=2) for i in range(len(cons_cord)-1)]


def stars(n, size=10, n_cons=5):

    coordinates_list = []
    for i in range(n):
        colour = choice(['yellow', 'white', 'orange', 'red', 'lightblue'])
        random_x, random_y = randint(0, WIDTH), randint(0, HEIGHT)

        if i < n_cons:
            coordinates_list.append([random_x, random_y])

        canvas.create_oval(random_x, random_y, random_x + size, random_y + size, fill=colour, outline=colour)

    constellation(coordinates_list)


def moon(x, y, img):
    canvas.create_image(x, y, image=img)


stars(randint(100, 1000))
moon_img = tk.PhotoImage(file='NightSky/tkinter_moon.png')
moon(550, 10, moon_img)

tk.mainloop()
