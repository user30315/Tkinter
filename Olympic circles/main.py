import tkinter as tk

WIDTH, HEIGHT = 650, 350
canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()

colours = ['blue', 'yellow', 'black', 'green', 'red']

for i in range(5):
    if i % 2 == 0:
        canvas.create_oval(50 + 100*i, 200, 200 + 100*i, 50, width=25, outline=colours[i])
    else:
        canvas.create_oval(250 + 100*(i-2), 275, 400 + 100*(i-2), 125, width=25, outline=colours[i])

tk.mainloop()
