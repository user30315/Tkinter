import tkinter as tk
import random

WIDTH, HEIGHT = 600, 400
canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()

def rectangles():
    rects = []
    for _ in range(2):
        x1 = random.randint(0, WIDTH-150)
        y1 = random.randint(0, HEIGHT-150)
        x2 = x1 + random.randint(50, 150)
        y2 = y1 + random.randint(50, 150)
        rects.append((x1, y1, x2, y2))
    
    intersection = rects[0] != rects[1] and (rects[0][0] < rects[1][2] and rects[0][2] > rects[1][0] and rects[0][1] < rects[1][3] and rects[0][3] > rects[1][1])
    
    for x1, y1, x2, y2 in rects:
        canvas.create_rectangle(x1, y1, x2, y2, fill="orange" if intersection else "green", outline="")
        
    if intersection:
        intersection_x1 = max(rects[0][0], rects[1][0])
        intersection_y1 = max(rects[0][1], rects[1][1])
        intersection_x2 = min(rects[0][2], rects[1][2])
        intersection_y2 = min(rects[0][3], rects[1][3])
        canvas.create_rectangle(intersection_x1, intersection_y1, intersection_x2, intersection_y2, fill="red", outline="")


rectangles()

tk.mainloop()
