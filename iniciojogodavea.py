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

def tela():
    global velha
    global jogadas 
    os.system("cls")
    print("     0   1   2")
    print(" 0 |", velha[0][0], "|", velha[0][1], "|", velha[0][2],"|")
    print(" 1 |", velha[1][0], "|", velha[1][1], "|", velha[1][2],"|")
    print(" 2 |", velha[2][0], "|", velha[2][1], "|", velha[2][2],"|")
    
    
def playerJoga():
    global jogadas
    global player
    global maxJogadas
    
    if player == 2 and jogadas < maxJogadas:
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
         
         
def CPUJoga():
    global jogadas
    global player
    global maxJogadas
    
    if player == 1 and jogadas < maxJogadas:
            l = random.randrange(0,3)
            c = random.randrange(0, 3)
            while velha[l][c] != " ":
                l = random.randrange(0,3)
                c = random.randrange(0, 3)
            velha[l][c] = "O"
            player = 2
            jogadas += 1
            
def verificaVitoria():
    global velha
    vit = "n"
    simbolos = ["X", "O"]
    
    for s in simbolos:
        vit = "n"
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
                if soma == 3:
                    vitoria = s
                    break
            il += 1
        return vitoria


          
                    
        
        
while True:                 
    tela()
    playerJoga()
    CPUJoga()
    tela()    
    vit = verificaVitoria()
    
    if(vit != "n" or jogadas >= maxJogadas):
        break
print("FIM.")
if vit == "X" or vit =="O":
    print("Resultado: Jogador", vit, "Venceu! ")
else:
    print("Resultado empate.")
