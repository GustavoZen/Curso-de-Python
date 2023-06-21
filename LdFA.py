import time
import os
import random
from tkinter import *
from tkinter import ttk
from sqlite3 import Error
import sqlite3

def Printar_Lista(lista):
    for i in range(len(lista)):
        if i != len(lista) - 1:
            print(f"{lista[i]}", end=", ")
        else:
            print(f"{lista[i]}")

def Somar_Lista(lista):
    soma = 0
    for element in lista:
        soma += element
    return soma

def Delay(s):
    time.sleep(s)

def Printar_Matriz(Matriz):
    for linha in Matriz:
        Printar_Lista(linha)
  
def Somar_Matriz(Matriz):
    soma = 0
    for linha in Matriz:
        soma += Somar_Lista(linha)
    return soma

def contar_nums_maior_que_x_na_matriz(num,matriz):
    contador = 0
    for linha in matriz:
        for element in linha:
            if(element > num):
                contador += 1
    return contador

def centralizar_janela(window):
    width = window.winfo_reqwidth()
    height = window.winfo_reqheight()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))
    return f"{width}x{height}+{x}+{y}"

def conexaoBanco(string): 
    pastaApp = os.path.dirname(__file__)
    caminho = pastaApp + "\\"+ string
    
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

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
