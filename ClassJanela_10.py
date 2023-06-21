from tkinter import *
from LdFA import *

class ClassJanela():

    def __init__(self,title,largura,altura,corbg):
        self.janela = Tk()
        self.janela.title(title)
        self.janela.configure(width=largura,height=altura,bg=corbg)
        self.janela.geometry(centralizar_janela(self.janela))