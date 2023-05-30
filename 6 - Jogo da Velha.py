import os
import random


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
    print("     0   1   2")
    print(" 0 |", velha[0][0], "|", velha[0][1], "|", velha[0][2],"|")
    print(" 1 |", velha[1][0], "|", velha[1][1], "|", velha[1][2],"|")
    print(" 2 |", velha[2][0], "|", velha[2][1], "|", velha[2][2],"|")
    
def verificaVitoriaLinha(s):
    global velha
    somalinha = 0
    for l in range(3):
        somalinha = 0
        for c in range(3):
            if velha[l][c] == s:
                somalinha += 1
            if somalinha >= 3:
                return s
    return "n"

def verificaVitoriaColuna(s):
    global velha
    somacoluna = 0
    for c in range(3):
        somacoluna = 0
        for l in range(3):
            if velha[l][c] == s:
                somacoluna += 1
            if somacoluna >= 3:
                return s
    return "n"
                
def verificaVitoriaDiagonal(s):
    global velha
    if (velha[0][0] == s and velha[1][1] == s and velha[2][2] == s) or (velha[2][0] == s and velha[1][1] == s and velha[0][2] == s):
        return s
    else:
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
        
        
while True:                 
    tela()
    if player == 2:
        playerJoga()
    else:
        CPUJoga()
    tela()
    
    if(vit != "n" or jogadas >= maxJogadas):
        break
print("FIM.")
if vit == "X" or vit =="O":
    print("Resultado: Jogador", vit, "Venceu! ")
else:
    print("Resultado empate.")