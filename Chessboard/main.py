import tkinter as tk

WIDTH = HEIGHT = 402
canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()

colours, colour = ['', 'white', 'black'], 1
for i in range(8):
    colour *= -1
    for j in range(8):
        colour *= -1
        canvas.create_rectangle(3 + j*50, 3 + i*50, 53 + j*50, 53 + i*50, fill=colours[colour])

tk.mainloop()
