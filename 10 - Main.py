from tkinter import *  
import os
from ClassJanela_10 import ClassJanela

Entradas = []
nome = ""
Senha = ""
Telefone = ""
Email = ""
def salvar_dados():
    global nome
    global Senha
    global Telefone
    global Email
    for element in Entradas:
        if element[0] == "Nome":
            nome = element[1].get()
        elif element[0] == "Telefone":
            Telefone = element[1].get()
        elif element[0] == "Email":
            Email = element[1].get()

config = ClassJanela("Mudar Senha", "500x300", "#243447")

config.add_label("Senha antiga", "#243447", "White", 10, 10)
config.add_label("Nova Senha", "#243447", "White", 10, 60)
config.add_label("Confirmar Nova Senha", "#243447", "White", 10, 110)
config.add_entry("*", 10, 30,"Senha Antiga")
config.add_entry("*", 10, 80,"Nova Senha")
config.add_entry("*", 10, 130,"Confirmar Nova Senha")

perfil = ClassJanela("Senac", "500x300", "#243447")

perfil.add_label("Nome", "#243447", "White", 10, 10)
perfil.add_entry("", 10, 30,"Nome")
perfil.add_label("Telefone", "#243447", "White", 10, 60)
perfil.add_entry("", 10, 80,"Telefone")
perfil.add_label("Email", "#243447", "White", 10, 110)
perfil.add_entry("", 10, 130,"Email")
perfil.add_label("Senha", "#243447", "White", 10, 160)
perfil.add_entry("", 10, 180,"Senha")
perfil.add_button("Salvar","#FFFFFF","Black",salvar_dados,10,270)

def open_Window(windowroot,data):
    newwindow = Toplevel(windowroot)
    newwindow.title(data.title)
    newwindow.geometry(data.geometry)
    newwindow.configure(background= data.corbg)
    global Entradas
    for element in data.Labels:
        Label(newwindow,text=element[0],bg=element[1],fg=element[2],anchor="w").place(x=element[3],y=element[4], width=300,height=20)
    for element in data.Entries:
        var = StringVar()
        entry = Entry(newwindow, show=element[0], textvariable=var).place(x=element[1], y=element[2])
        Entradas.append([element[3], var, entry])
    for element in data.Buttons:
        Button(newwindow,text=element[0],bg=element[1],fg=element[2],command=element[3]).place(x=element[4],y=element[5])

app = Tk()
app.title("Senac")
app.geometry("500x300")
corbg = "#243447"
app.configure(background=corbg)
menu = Menu(app, tearoff=0)
app.config(menu=menu)
menu_perfil = Menu(menu, tearoff=0)
menu.add_cascade(label="Perfil", menu=menu_perfil)
menu_perfil.add_command(label="Acessar", command=lambda:open_Window(app,perfil))

menu_Config = Menu(menu, tearoff=0)
menu.add_cascade(label="Config", menu=menu_Config)
menu_Config.add_command(label="Mudar Senha", command=lambda:open_Window(app,config))


app.mainloop()