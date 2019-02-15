from tkinter import *
from tkinter import messagebox
from tkinter import  ttk
import pickle
import re

troj = False
kolo = False
kwadrat = False

sec = Tk()
sec.geometry("300x315")
sec.title("Zarejestruj sie")
canvas = Canvas(sec, width=300, height=300)
canvas.pack()
imie = ttk.Entry(width=32)
login = ttk.Entry(width=32)
email = ttk.Entry(width=32)
passworld = ttk.Entry(width=32, show = '*')
passworld2 = ttk.Entry(width=32, show = '*')
button = ttk.Button(width=25, text = "Rejestruj", command=lambda: save())
canvas.create_text(150, 33, text="Imie Nazwisko", font="Arial 14")
canvas.create_text(150, 80, text="Nazwa urzytkownika", font="Arial 14")
canvas.create_text(150, 127, text="E-mail", font="Arial 14")
canvas.create_text(150, 174, text="Hasło", font="Arial 14")
canvas.create_text(150, 221, text="Powtórz hasło", font="Arial 14")
imie.place(x=55, y=48)
login.place(x=55, y=93)
email.place(x=55, y=139)
passworld.place(x=55, y=185)
passworld2.place(x=55, y=231)
button.place(x=70, y= 270)
def save():
    has_special = re.compile("|".join(map(re.escape, ".,:;!_*-+()/#¤@%&)"))).search
    has_at = re.compile("|".join(map(re.escape, "@"))).search
    if login.get() == "":
        messagebox.showerror("Error!", "Musisz podać nazwę urzytkownika")
    elif not bool(has_at(email.get())):
        messagebox.showerror("Error!", "Podałesz nieprawidłowy e-mail adres")
    elif passworld.get() != passworld2.get():
        messagebox.showerror("Error!", "Musisz podać jednakowe hasło")
    elif len(passworld.get()) < 5:
        messagebox.showerror("Error!", "Hasło musi zawierać więcej niż 6 znaków")
    elif bool(has_special(passworld.get())):
        messagebox.showerror("Error!", "Hasło nie musi zawierac .,:;!_*-+()/#¤@%&)")
    else:
        login_pass_save = {login.get(): passworld.get()}
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        sec.destroy()
        loginf()

def loginf():
    log_form = Tk()
    log_form.geometry("300x300")
    log_form.title("Zaloguj się")
    canvas = Canvas(log_form, width=300, height=300)
    canvas.pack()
    canvas.create_text(150, 58, text="Nazwa urzytkownika", font="Arial 14")
    canvas.create_text(150, 105, text="Hasło", font="Arial 14")
    enter_login = ttk.Entry(width=32)
    enter_pass = ttk.Entry(width=32, show = "*")
    batton = ttk.Button(width=25, text = "Zaloguj sie", command=lambda: log_pass())
    enter_login .place(x=55, y=70)
    enter_pass.place(x=55, y=115)
    batton.place(x=72, y=160)

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                messagebox.showinfo("Witam!", "Świetnej gry, "+ enter_login.get() +"!!")
                log_form.destroy()

                canvas_width = 1000
                canvas_height = 600
                back = "white"

                def paint(event):
                    x1 = event.x - int(variable2.get())
                    x2 = event.x + int(variable2.get())
                    y1 = event.y - int(variable2.get())
                    y2 = event.y + int(variable2.get())
                    w.create_oval(x1, y1, x2, y2,
                                  fill=variable.get(), outline=variable.get())

                def draw(event):
                    global  kolo, kwadrat, troj
                    if kolo:
                        w.create_oval(event.x - int(variable3.get()), event.y - int(variable3.get()),
                                      event.x + int(variable3.get()), event.y + int(variable3.get()),
                                      fill=variable.get(), outline=variable.get())
                    elif kwadrat:
                        w.create_rectangle(event.x, event.y, event.x + int(variable3.get())*2,
                                           event.y + int(variable3.get())*2, fill=variable.get(),
                                           outline=variable.get())
                    elif troj:
                        points = [event.x, event.y-int(variable3.get())*1.5, event.x+int(variable3.get())*1.5,
                                  event.y+int(variable3.get())*1.5, event.x-int(variable3.get())*1.5,
                                  event.y+int(variable3.get())*1.5]
                        w.create_polygon(points, outline=variable.get(),
                                        fill=variable.get())

                def button_pressed(button):
                    global kolo, kwadrat, troj
                    if button["text"] == "Kolo":
                        kolo = True
                        kwadrat = False
                        troj = False
                    elif button["text"] == "Kwadrat":
                        kwadrat = True
                        troj = False
                        kolo = False
                    elif button["text"] == "Trojkat":
                        troj = True
                        kolo = False
                        kwadrat =False

                def erase():
                    variable.set(back)
                    return variable

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

                w = Canvas(root, width=canvas_width,
                           height=canvas_height, bg=back)
                w.bind("<B1-Motion>", paint)
                w.bind("<Button-3>", draw)

                variable = StringVar(root)
                variable.set("black")  # default value
                a = OptionMenu(root, variable, "red", "green", "blue", "yellow", "pink", "purple", "grey", "orange",
                               "brown", "gold", "lime")
                a.config(width=7)
                a.grid(row=0, column=0)

                variable2 = StringVar(root)
                variable2.set("3")  # default value
                a2 = OptionMenu(root, variable2, "1", "2", "3", "4", "5", "6", "8", "10")
                a2.config(width=7)
                a2.grid(row=0, column=1)

                variable3 = StringVar(root)
                variable3.set("30")  # default value
                a3 = OptionMenu(root, variable3, "10", "20", "30", "40", "50", "60", "80", "90", "100")
                a3.config(width=7)
                a3.grid(row=0, column=4)

                erase_btn = Button(text="Eraser", width=10,
                                   command=lambda: erase())
                erase_btn.grid(row=0, column=2)

                clear_btn = Button(text="Clear all", width=10,
                                   command=lambda: w.delete("all"))
                clear_btn.grid(row=0, column=8)

                siatka_btn = Button(text="Siatka", width=10,
                                    command=lambda: siatka(int(variable3.get()),
                                                           int(variable3.get()), variable.get(), int(variable2.get())))
                siatka_btn.grid(row=0, column=3)

                kwadrat_btn = Button(text="Kwadrat", width=10, command=lambda: button_pressed(kwadrat_btn))
                kwadrat_btn.grid(row=0, column=6)

                kolo_btn = Button(text="Kolo", width=10, command=lambda: button_pressed(kolo_btn))
                kolo_btn.grid(row=0, column=7)

                tr_btn = Button(text="Trojkat", width=10, command=lambda: button_pressed(tr_btn))
                tr_btn.grid(row=0, column=5)

                w.grid(row=1, column=0,
                       columnspan=9, padx=5,
                       pady=5, sticky=E + W + S + N)
                w.columnconfigure(9, weight=1)
                w.rowconfigure(2, weight=1)
                root.mainloop()

            else: messagebox.showerror("Error", "Podałesz nieprawidłowe hasło")
        else: messagebox.showerror("Error!", "Nieprawidłowa nazwa urzytkownika")

sec.mainloop()
