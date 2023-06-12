from tkinter import*
from ClassJanela_10 import ClassJanela

app = ClassJanela("Teste", "500x300", "#dde")

vfutebol = IntVar()
vvolei = IntVar()

def futebolClicado():
    print("Futebol: ", vfutebol.get())

def voleiClicado():
    print("Volei: ", vvolei.get())

fr_quadro = Frame(app, borderwidth=1, relief="solid")
fr_quadro.place(x=10, y=10, width=300, height=100)

cb_futebol = Checkbutton(fr_quadro, text="Futebol", variable=vfutebol, onvalue=1, offvalue=0, command=futebolClicado)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(fr_quadro, text="Vôlei", variable=vvolei, onvalue=1, offvalue=0, command=voleiClicado)
cb_volei.pack(side=LEFT)

app.mainloop()