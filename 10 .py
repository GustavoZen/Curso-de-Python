from tkinter import *  
import os

c = os.path.dirname(__path__)
nomeArquivo = c+"\\data.txt"

def impDdos():
    arquivo = open(nomeArquivo, "a")
    arquivo.write("Nome....: %s" % vnome.get())
    arquivo.write("Telefone: %s" % vtelefone.get())
    arquivo.write("Email...: %s" % vemail.get())
    #arquivo.write("OBS.....: %s" % vobs.get("1.0",END))
    arquivo.write("\n")
    arquivo.close()


app = Tk()
app.title("Senac")
app.geometry("500x300")
corbg = "#dde"
app.configure(background=corbg)

Label(app, text = "Nome", bg = corbg, fg = "#009", anchor = "w").place(x=10,y=10, width=100,height=20)
vnome = Entry(app)
vnome.place(x = 10,y = 30, width = 200, height = 20)

Label(app, text = "Telefone", bg = corbg, fg = "#009", anchor = "w").place(x=10,y=60, width=100,height=20)
vtelefone = Entry(app)
vtelefone.place(x = 10,y = 80, width = 200, height = 20)

Label(app, text = "Email", bg = corbg, fg = "#009", anchor = "w").place(x=10,y=110, width=100,height=20)
vemail = Entry(app)
vemail.place(x = 10,y = 130, width = 300, height = 20)

Button(app,text = "Salvar", bg = "#FFFFFF", fg="Black").place(x = 10, y = 270, width = 100, height = 20)

app.mainloop()
