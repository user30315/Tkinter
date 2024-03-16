import tkinter as tk

FLAG_WIDTH, FLAG_HEIGHT = 205, 140
WIDTH, HEIGHT = 200+2*FLAG_WIDTH, 200+2*FLAG_HEIGHT
canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bg="#f0f0f0")
canvas.pack()

class Flag():

    def __init__(self, x, y, flag_width = FLAG_WIDTH, flag_height = FLAG_HEIGHT):
        self.x, self.y = x, y
        self.flag_width, self.flag_height = flag_width, flag_height

    def draw_flag(self, horizontal: bool, number_of_stripes: int, stripe_colours: tuple):

        for i in range(number_of_stripes):
            if horizontal:
                stripe_height = self.flag_height/number_of_stripes
                canvas.create_rectangle(self.x, self.y + i*stripe_height, self.x + self.flag_width, self.y + (i+1)*stripe_height, 
                                        fill=stripe_colours[i], width=0)
            else:
                stripe_width = self.flag_width/number_of_stripes
                canvas.create_rectangle(self.x + i*stripe_width, self.y + FLAG_HEIGHT, self.x + (i+1)*stripe_width, self.y,
                                        fill=stripe_colours[i], width=0)

        canvas.create_rectangle(self.x, self.y, self.x + self.flag_width, self.y + self.flag_height, width=1.5)

germany = Flag(50, 50)
germany.draw_flag(True, 3, ("#000000", "#DB0000", "#FFCC00"))

italy = Flag(150 + FLAG_WIDTH, 50)
italy.draw_flag(False, 3, ("#008C45", "#F4F4FF", "#CD212A"))

france = Flag(50, 150 + FLAG_HEIGHT)
france.draw_flag(False, 3, ("#0055A4", "#FFFFFF", "#EF4135"))

ukraine = Flag(150 + FLAG_WIDTH, 150 + FLAG_HEIGHT)
ukraine.draw_flag(True, 2, ("#005888", "#FFD500"))


tk.mainloop()

