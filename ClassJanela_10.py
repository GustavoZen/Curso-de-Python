from tkinter import *

class ClassJanela():

    def __init__(self,title,tamanho,corbg):
        self.title = title
        self.geometry = tamanho
        self.corbg = corbg
        self.Labels =    []
        self.Buttons =   []
        self.Entries =   []

    
    def add_button(self, text, bg, fg, command, x, y):
        a = [text,bg,fg,command,x,y]
        self.Buttons.append(a)

    def add_label(self, text, bg, fg, x, y):
        a = [text,bg,fg,x,y]
        self.Labels.append(a)

    def add_entry(self, show, x, y,var):
        a = [show,x,y,var]
        self.Entries.append(a)