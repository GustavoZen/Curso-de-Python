import LdFA
import os
import random
import time

#Calcular a média (list, input)
os.system('cls')
lista = []
total = 0
while True:
    num = int(input("Digite um número para adicionar à lista: (0 = saída)"))
    if num == 0:
        break
    else:
        lista.append(num)
for element in lista:
    total += element
media = total/len(lista)
LdFA.Printar_Lista(lista)
print("A média dos números contidos na lista é: {}".format(media))
LdFA.Delay

#Verificar 3x se acertou a senha
senha = 2449
i=0
while i<3:
    teste = float(input("Digite a senha: "))
    if teste == senha:
        print("Bem Vindo!\nUsuário Logado")
        break
    else:
        print("Senha Incorreta!")
    if i==2:
        print("Numero máximo de Tentativas alcançado, Usuário bloqueado")
    i+=1
#Adaptar jogo da adivinhação
numero_oculto = random.randint(1, 100)
tentativas_max = int(input("Quantas tentativas você terá: "))
i = 0
while i < tentativas_max:

    chute = int(input("Digite seu {} chute: ".format(i+1)))
    if chute > numero_oculto:
        os.system('cls')
        print("O número a ser adivinhado é menor que o chute ({}).".format(chute))
    elif chute < numero_oculto:
        os.system('cls')
        print("O número a ser adivinhado é maior que o chute ({}).".format(chute))
    
    else:
        print(f"Parabêns! Você adivinhou o número oculto em {i+1} tentativas")
        break
    if i+1 == tentativas_max:
        print("Estourou o número máximo de tentativas, Você perdeu.")
    i+=1
