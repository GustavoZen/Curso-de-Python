import time
import os
import random


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