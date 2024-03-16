import tkinter as tk

canvas = tk.Canvas(width=420, height=200)
canvas.pack()

def draw_zigzag(x, y, num_lines=20, line_length=20, colour="blue"):
    x_start, y_start = x, y
    x_end, y_end = x_start, y_start
    direction = 1
    for _ in range(num_lines):
        canvas.create_line(x_start, y_start, x_end, y_end, fill=colour, width=2)
        x_start, y_start = x_end, y_end
        x_end += line_length
        y_end = y_start + (line_length * direction)
        direction *= -1


for i in range(3):
    draw_zigzag(20, 20 + 40*i)

tk.mainloop()
