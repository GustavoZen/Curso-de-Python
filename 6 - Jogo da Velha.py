import os
import random
from LdFA import Delay
from colorama import Fore

resposta = 0
velha =[
    [" "," "," ",],
    [" "," "," ",],
    [" "," "," ",]

]

jogadas = 0

maxJogadas = 9

player = 2 # CPU = 1 | player = 2

vit = "n"

def tela():
    global velha
    global jogadas 
    os.system("cls")
    print(Fore.RESET, "     0     1     2")
    for i in range(3):
        print(f" {i}  ",end = "")
        for indice,element in enumerate(velha[i]):
            if element == "X" and indice != 2:
                print(Fore.RED, f" {element}", Fore.RESET, "|", end = "")
                Fore.RESET
            elif element == "O" and indice != 2:
                print(Fore.GREEN, f" {element}", Fore.RESET, "|", end = "")
                Fore.RESET
            elif element == "X" and indice == 2:
                print(Fore.RED, f" {element}", Fore.RESET, end = "")
                Fore.RESET
            elif element == "O" and indice == 2:
                print(Fore.GREEN, f" {element}", Fore.RESET, end = "")
                Fore.RESET
            elif indice !=2 :
                print(Fore.RESET, "    |", end = "")
            else:
                print(Fore.RESET, "     ", end = "")
        if i != 2:
            print("\n     ----------------\n", end = "")
        else:
            print("")
    
def verificaVitoriaLinha(s):
    global velha
    for l in range(3):
        if (velha[l][0] == s and velha[l][1] == s and velha[l][2] == s):
                return s
    return "n"

def verificaVitoriaColuna(s):
    global velha
    for c in range(3):
        if (velha[0][c] == s and velha[1][c] == s and velha[2][c] == s):
                return s
    return "n"
                
def verificaVitoriaDiagonal(s):
    global velha
    if (velha[0][0] == s and velha[1][1] == s and velha[2][2] == s) or (velha[2][0] == s and velha[1][1] == s and velha[0][2] == s):
        return s
    return "n"

def verificaVitoria(s):
    global velha
    global vit
    if verificaVitoriaLinha(s) == s or verificaVitoriaColuna(s) == s or verificaVitoriaDiagonal(s) == s:
        vit = s
    else:
        vit = "n"    
    
def player2Joga():
    global jogadas
    global player
    global maxJogadas
    simbolo = "O"
    
    if jogadas < maxJogadas:
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
            while velha[l][c] != " ":
                l = int(input("Linha: "))
                c = int(input("Coluna: "))
            velha[l][c] = simbolo
            player = 2
            jogadas += 1
                
        except:
            print("linha ou coluna invalida!.!" )
            os.system("pause")
    verificaVitoria(simbolo)
                 
def playerJoga():
    global jogadas
    global player
    global maxJogadas
    simbolo = "X"
    
    if jogadas < maxJogadas:
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
            while velha[l][c] != " ":
                l = int(input("Linha: "))
                c = int(input("Coluna: "))
            velha[l][c] = "X"
            player = 1
            jogadas += 1
                
        except:
            print("linha ou coluna invalida!.!" )
            os.system("pause")
    verificaVitoria(simbolo)
                 
def CPUJoga():
    global jogadas
    global player
    global maxJogadas
    simbolo = "O"
    if jogadas < maxJogadas:
            l = random.randrange(0,3)
            c = random.randrange(0, 3)
            while velha[l][c] != " ":
                l = random.randrange(0,3)
                c = random.randrange(0, 3)
            velha[l][c] = simbolo
            player = 2
            jogadas += 1
    verificaVitoria(simbolo)
        
def reset():
    global jogadas
    global velha
    global player
    global vit
    vit = "n"
    player = 2
    velha =[
    [" "," "," ",],
    [" "," "," ",],
    [" "," "," ",]
    ]
    jogadas = 0

def game():                 
    while True:
        tela()
        if player == 2:
            playerJoga()
        else:
            CPUJoga()
            Delay(0.5)
        tela()
        
        if(vit != "n" or jogadas >= maxJogadas):
            print("FIM.")
            if vit == "X" or vit =="O":
                print("Resultado: Jogador", vit, "Venceu! ")
                break
            else:
                print("Resultado empate.")
                break

game()
resposta = input("Deseja Jogar Novamente?[y/n]")
while resposta != "n" and resposta != "N":
    Delay(1)
    reset()
    game()
    resposta = input("Deseja Jogar Novamente?[y/n]")
