import tkinter as tk

WIDTH, HEIGHT = 575, 402
canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bg="#f0f0f0")
canvas.pack()

x, y = 15, 300
colours = ["#cf262c","#405034", "#23d887", "#b29211", "#8c0fb2", "#ae624b", "#81b4f2", "#eeece0"]
for i in range(15, 135, 15):
    canvas.create_rectangle(x, y, x + i, y - i, fill=colours[(i//15)-1], width=1.5)
    x += i

tk.mainloop()
