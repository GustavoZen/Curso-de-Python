import random
import os
numero_oculto = random.randint(1, 100)
tentativas_jogador=0
tentativas_maquina=0
chute = 0
while chute != numero_oculto:
    chute = int(input("Digite seu {} chute: ".format(tentativas_jogador+1)))
    if chute > numero_oculto:
        os.system('cls')
        print("O número a ser adivinhado é menor que o chute ({}).".format(chute))
    elif chute < numero_oculto:
        os.system('cls')
        print("O número a ser adivinhado é maior que o chute ({}).".format(chute))
    else:
        print(f"Parabêns! Você adivinhou o número oculto em {tentativas_jogador+1} tentativas")
        break
    tentativas_jogador+=1

#Maquina adivinha o número aprendendo
piso = 0
teto = 100
chute = 0
while chute != numero_oculto:

    chute =  random.randint(piso, teto)
    if chute > numero_oculto:
        print("O número a ser adivinhado é menor que o chute ({}).".format(chute))
        teto = chute - 1
    elif chute < numero_oculto:
        print("O número a ser adivinhado é maior que o chute ({}).".format(chute))
        piso = chute + 1
    else:
        print(f"Parabêns! Você adivinhou o número oculto em {tentativas_maquina+1} tentativas")
        break
    tentativas_maquina+=1

