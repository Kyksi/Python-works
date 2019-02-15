from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pickle
import random
import re


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


root = Tk()
root.geometry("485x340")
root.title("SZUBIENICA")
center(root)


def first_okno():
    global logo
    logo = PhotoImage(file="first.gif")
    logo1 = Label(root, image=logo)
    logo1.place(x=0, y=0)
    button_next = ttk.Button(text="Dalej", width=25, command=lambda: rejestracja())
    button_cancel = ttk.Button(text="Zamknij", width=25, command=lambda: exit(0))
    button_next.place(x=60, y=300)
    button_cancel.place(x=260, y=300)


def rejestracja():
    root.destroy()
    sec = Tk()
    sec.geometry("300x300")
    sec.title("Zarejestruj sie")
    center(sec)
    canvas = Canvas(sec, width=300, height=300)
    canvas.pack()
    y = 0
    while y < 300:
        x = 0
        while x < 300:
            canvas.create_rectangle(x, y, x + 28, y + 23,
                                    fill="white", outline="blue")
            x = x + 28
        y = y + 23
    imie = ttk.Entry(width=32)
    login = ttk.Entry(width=32)
    email = ttk.Entry(width=32)
    passworld = ttk.Entry(width=32, show='*')
    passworld2 = ttk.Entry(width=32, show='*')
    button = ttk.Button(width=25, text="Rejestruj", command=lambda: save())
    canvas.create_text(150, 33, text="Imie Nazwisko", fill="purple", font="Arial 14")
    canvas.create_text(150, 80, text="Nazwa urzytkownika", fill="purple", font="Arial 14")
    canvas.create_text(150, 127, text="E-mail", fill="purple", font="Arial 14")
    canvas.create_text(150, 174, text="Hasło", fill="purple", font="Arial 14")
    canvas.create_text(150, 221, text="Powtórz hasło", fill="purple", font="Arial 14")
    imie.place(x=55, y=48)
    login.place(x=55, y=93)
    email.place(x=55, y=139)
    passworld.place(x=55, y=185)
    passworld2.place(x=55, y=231)
    button.place(x=70, y=260)

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
    center(log_form)
    canvas = Canvas(log_form, width=300, height=300)
    canvas.pack()
    y = 0
    while y < 300:
        x = 0
        while x < 300:
            canvas.create_rectangle(x, y, x + 28, y + 23,
                                    fill="white", outline="blue")
            x = x + 28
        y = y + 23
    canvas.create_text(150, 58, text="Nazwa urzytkownika", fill="purple", font="Arial 14")
    canvas.create_text(150, 105, text="Hasło", fill="purple", font="Arial 14")
    enter_login = ttk.Entry(width=32)
    enter_pass = ttk.Entry(width=32, show="*")
    batton = ttk.Button(width=25, text="Zaloguj sie", command=lambda: log_pass())
    enter_login.place(x=55, y=70)
    enter_pass.place(x=55, y=115)
    batton.place(x=72, y=160)

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                messagebox.showinfo("Witam!", "Świetnej gry, " + enter_login.get() + "!!")
                log_form.destroy()

                game_window = Tk()
                game_window.title("Szubienica!")
                canvas = Canvas(game_window, width=600, height=600)
                canvas.pack()
                center(game_window)

                def but():
                    y = 0
                    while y < 600:
                        x = 0
                        while x < 600:
                            canvas.create_rectangle(x, y, x + 33, y + 27,
                                                    fill="white", outline="blue")
                            x = x + 33
                        y = y + 27
                    canvas.create_line(5, 10, 5, 500, width=4)
                    canvas.create_line(3, 10, 165, 10, width=4)
                    canvas.create_line(5, 70, 70, 10, width=4)

                faq = '''             Gracz stara się odgadnąć litery słowa. Za każdym razem,\n
                         gdy mu się to uda, pierwszy gracz wstawia literę \n
                         w odpowiednie miejsce; w przeciwnym wypadku rysuje \n
                         element symbolicznej szubienicy i wiszącego na \n
                         niej ludzika. Jeżeli pierwszy gracz narysuje kompletnego \n
                         „wisielca” zanim drugi odgadnie słowo, wówczas wygrywa. \n
                         W zależności od wcześniej ustalonego stopnia skomplikowania \n
                         rysunku „wisielca” (liczba elementów potrzebna do jego \n
                         narysowania), gra pozwala na mniej lub więcej pomyłek.'''
                canvas.create_text(270, 240, text=faq, fill="purple", font="Arial 14")

                words = ["pijalnia", "paluszek", "ekologia", "serowiec", "dziękuje", "dobranoc", "listopad", "kiełbasa"
                                                                                                             "dwunasta",
                         "południe", "pojutrze", "czwartek", "czerwony", "kwiecień", "czerwiec"]

                def arr():
                    but()
                    word = random.choice(words)
                    w = word[1:-1]
                    wor = []

                    for i in w:
                        wor.append(i)
                    canvas.create_text(282, 40, text=word[0], fill="purple", font="Arial 18")
                    canvas.create_text(315, 40, text="__", fill="purple", font="Arial 18")
                    canvas.create_text(347, 40, text="__", fill="purple", font="Arial 18")
                    canvas.create_text(380, 40, text="__", fill="purple", font="Arial 18")
                    canvas.create_text(412, 40, text="__", fill="purple", font="Arial 18")
                    canvas.create_text(444, 40, text="__", fill="purple", font="Arial 18")
                    canvas.create_text(477, 40, text="__", fill="purple", font="Arial 18")
                    canvas.create_text(510, 40, text=word[-1], fill="purple", font="Arial 18")

                    list1 = [1, 2, 3, 4, 5, 6]
                    alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
                    er = []
                    win = []

                    def a(v):
                        ind_alf = alfabet.index(v)
                        key = alfabet[ind_alf]

                        if v in wor:
                            ind = wor.index(v)
                            b2 = list1[ind]
                            wor[ind] = "1"

                            def kord():
                                global x1, y1
                                if b2 == 1:
                                    x1, y1 = 315, 40
                                if b2 == 2:
                                    x1, y1 = 347, 40
                                if b2 == 3:
                                    x1, y1 = 380, 40
                                if b2 == 4:
                                    x1, y1 = 412, 40
                                if b2 == 5:
                                    x1, y1 = 444, 40
                                if b2 == 6:
                                    x1, y1 = 477, 40
                                return x1, y1

                            x1, y1 = kord()
                            win.append(v)
                            a2 = canvas.create_text(x1, y1, text=w[ind], fill="purple", font=("Arial 18"))
                            btn[key]["bg"] = "lime"
                            if not v in wor:
                                btn[key]["state"] = "disabled"
                            if v in wor:
                                win.append(v)
                                ind2 = wor.index(v)
                                b2 = list1[ind2]
                                x1, y1 = kord()
                                canvas.create_text(x1, y1, text=w[ind2], fill="purple", font=("Arial 18"))
                            if len(win) == 6:
                                canvas.create_text(380, 350, text="You are win!!!", fill="purple", font="Arial 32")
                                for i in alfabet:
                                    btn[i]["state"] = "disabled"
                        else:
                            er.append(v)
                            btn[key]["bg"] = "red"
                            btn[key]["state"] = "disabled"
                            if len(er) == 1:
                                draw_head()
                            elif len(er) == 2:
                                draw_body()
                            elif len(er) == 3:
                                draw_left_hand()
                            elif len(er) == 4:
                                draw_right_hand()
                            elif len(er) == 5:
                                draw_left_lag()
                            elif len(er) == 6:
                                draw_right_lag()
                                lose()

                    btn = {}

                    def gen(u, x, y):
                        btn[u] = Button(game_window, text=u, width=3, height=1, command=lambda: a(u))
                        btn[u].place(x=str(x), y=str(y))

                    x = 265
                    y = 110
                    for i in alfabet[0:8]:
                        gen(i, x, y)
                        x += 33
                    x = 265
                    y = 137
                    for i in alfabet[8:16]:
                        gen(i, x, y)
                        x += 33
                    x = 265
                    y = 164
                    for i in alfabet[16:24]:
                        gen(i, x, y)
                        x += 33
                    x = 265
                    y = 191
                    for i in alfabet[24:32]:
                        gen(i, x, y)
                        x += 33

                    def draw_head():
                        canvas.create_oval(130, 100, 190, 155, width=4, fill="white")
                        canvas.create_line(160, 10, 160, 100, width=4)

                    def draw_body():
                        canvas.create_line(160, 155, 160, 260, width=4)

                    def draw_left_hand():
                        canvas.create_line(160, 155, 115, 200, width=4)

                    def draw_right_hand():
                        canvas.create_line(160, 155, 205, 200, width=4)

                    def draw_left_lag():
                        canvas.create_line(160, 260, 105, 360, width=4)

                    def draw_right_lag():
                        canvas.create_line(160, 260, 205, 360, width=4)

                    def lose():
                        canvas.create_text(380, 350, text="You are loose!!!", fill="purple", font="Arial 32")
                        for i in alfabet:
                            btn[i]["state"] = "disabled"

                button_start = ttk.Button(game_window, text="Nowa gra!", width=20, command=lambda: arr())
                button_start.place(x=155, y=542)
                button_exit = ttk.Button(game_window, text="Zamknij", width=20, command=lambda: exit(0))
                button_exit.place(x=315, y=542)
                game_window.mainloop()

            else:
                messagebox.showerror("Error", "Podałesz nieprawidłowe hasło")
        else:
            messagebox.showerror("Error!", "Nieprawidłowa nazwa urzytkownika")


first_okno()
root.mainloop()
