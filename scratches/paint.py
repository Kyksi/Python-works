from tkinter import *

canvas_width = 700
canvas_height = 500
brush_size = 3
brush_color = "black"
back = "white"

def paint(event):
    x1 = event.x - int(variable2.get())
    x2 = event.x + int(variable2.get())
    y1 = event.y - int(variable2.get())
    y2 = event.y + int(variable2.get())
    w.create_oval(x1, y1, x2, y2,
                  fill = variable.get(), outline = variable.get())

def erase():
    variable.set(back)
    return  variable

def siatka(newX, newY, color, width):
    y = 0
    while y < canvas_height:
        x = 0
        while x < canvas_width:
            w.create_rectangle(x, y, x + newX, y + newY,
                                    fill=back, outline=color, width=width)
            x = x + newX
        y = y + newY

root = Tk()
root.title("Paint")

w = Canvas(root, width = canvas_width,
           height = canvas_height, bg = back)
w.bind("<B1-Motion>", paint)

variable = StringVar(root)
variable.set("black") # default value
a = OptionMenu(root, variable, "red", "green", "blue", "yellow", "pink", "purple", "grey", "orange", "brown", "gold", "lime")
a.config(width=7)
a.grid(row=0, column=0)

variable2 = StringVar(root)
variable2.set("3") # default value
a2 = OptionMenu(root, variable2, "1", "2", "3", "4", "5", "6", "8", "10")
a2.config(width=7)
a2.grid(row=0, column=1)

variable3 = StringVar(root)
variable3.set("30") # default value
a3 = OptionMenu(root, variable3, "10", "20", "30", "40", "50", "60", "80", "90", "100")
a3.config(width=7)
a3.grid(row=0, column=4)

erase_btn = Button(text = "Eraser", width = 10,
                    command=lambda: erase())
erase_btn.grid(row = 0, column = 2)


clear_btn = Button(text = "Clear all", width = 10,
                    command=lambda: w.delete("all"))
clear_btn.grid(row=0, column=3)

siatka_btn = Button(text = "Siatka", width = 10,
                    command=lambda: siatka(int(variable3.get()),
                    int(variable3.get()), variable.get(), int(variable2.get())))
siatka_btn.grid(row=0, column=5)

w.grid(row = 1, column = 0,
       columnspan = 7, padx = 5,
       pady = 5, sticky = E+W+S+N)
w.columnconfigure(6, weight = 1)
w.rowconfigure(2, weight = 1)
root.mainloop()