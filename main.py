from tkinter import *
from Medovina import *

ferment = Medovina()

window = Tk()
window.minsize(400,600)
window.resizable(False, True)
window.iconbitmap("icon.ico")
window.title("Medovina 1.0")

input_area = Frame(window)
input_area.pack()
button_area = Frame(window)
button_area.pack()
leaven_frame = LabelFrame(window, text = "Zákvas")
leaven_frame.pack()
receipe_frame = LabelFrame(window, text = "Recept")
receipe_frame.pack()
procedure_frame = LabelFrame(window, text = "Postup přípravy")
procedure_frame.pack()

# variable definiton
main_font = ("sans-serif, 11")
var = IntVar()

def receipe():
    if volume_entry.get():
        mead = Medovina(int(volume_entry.get()), var.get())
        mead_receipe["text"] = mead.recept()
    else:
        mead_receipe["text"] = "Zadejte objem kvasné nádoby."

def procedure():
    w2 = Tk()
    w2.minsize(600,600)
    w2.iconbitmap("icon.ico")
    w2.resizable(False,False)
    w2.title("Postup přípravy")

    frame_title = Frame(w2)
    frame_title.pack()
    frame_text = Frame(w2)
    frame_text.pack()

    title = Label(frame_title, text="Postup přípravy")
    title.grid(row=0,column=0, pady=5)
    text = Text(frame_text, width=110, height=34)
    with open('postup.txt', "r", encoding="utf8") as file:
        for row in file:
            text.insert(INSERT,row)
    text["state"] = DISABLED
    text.grid(row=1,column=0, padx=10, pady=5, sticky=E+W+N+S)

    scrollbar = Scrollbar(frame_text)
    scrollbar.grid(row=1,column=1,sticky=N+S)
    scrollbar.config(command=text.yview)

    w2.mainloop()

# Input area

label_volume = Label(input_area, text = "Objem kvasné nádoby", font=main_font)
label_volume.grid(row=0, column=0, padx=5, pady=10)

volume_entry = Entry(input_area, width=5, font=main_font)
volume_entry.grid(row=0, column=1, padx=5)

label_litre = Label(input_area, text="litrů",font=main_font)
label_litre.grid(row=0, column=2)

label_sweetness = Label(input_area, text = "Chuť výsledné medoviny", font=main_font)
label_sweetness.grid(row=1, column=0, padx=5, pady=5)

r1 = Radiobutton(input_area, text="Sladká", variable=var, value=1, font=main_font)
r1.grid(row=2, column=0, padx=5, sticky=W)
r2 = Radiobutton(input_area, text="Polo-sladká", variable=var, value=2, font=main_font)
r2.grid(row=3, column=0, padx=5, sticky=W)
r3 = Radiobutton(input_area, text="Polo-suchá", variable=var, value=3, font=main_font)
r3.grid(row=4, column=0, padx=5, sticky=W)
r4 = Radiobutton(input_area, text="Polo-suchá", variable=var, value=4, font=main_font)
r4.grid(row=5, column=0, padx=5, sticky=W)

# Button area

button = Button(button_area, text="Vytvoř recept", command=receipe, font=main_font)
button.grid(row=0, column=1, pady=5, ipadx=5, ipady=5)

# Receipe area

leaven_receipe = Label(leaven_frame, text=ferment.kvas(), width=40, font=main_font)
leaven_receipe.grid(row=0, column=0, sticky=W+E, pady=5, ipady=5, ipadx=5)

mead_receipe = Label(receipe_frame, text="Zadejte objem kvasné nádoby", width=40, font=main_font)
mead_receipe.grid(row=0, column=0, sticky=W+E, pady=5, ipady=5, ipadx=5)

mead_procedure = Label(procedure_frame, text="                         ", width=40, font=main_font)
mead_procedure.grid(row=0, column=0, sticky=W+E, pady=5, ipady=5, ipadx=5)

# Procedure area

procedure_button = Button(procedure_frame, text="Číst postup přípravy", command=procedure, font=main_font)
procedure_button.grid(row=0, column=0, pady=30, ipadx=5, ipady=5)

window.mainloop()