#somar uma lista de valores
preco = [10,51,62,5.9,47,86,10.8,99]
total = 0
for i in preco:
    total = total + i
media = total/len(preco)
print("Total: " + str(total))
print(f"Média : {total/len(preco):.2f}")
print("Média : {:.2f}".format(total/len(preco)))
print("Média : {:.2f}".format(media))
 
#3 tentativas para acertar uma senha
senha = 2449
for i in range(3):
    teste = float(input("Digite a senha: "))
    if teste == senha:
        print("Bem Vindo!\nUsuário Logado")
        break
    else:
        print("Senha Incorreta!")
    if i==2:
        print("Numero máximo de Tentativas alcançado, Usuário bloqueado")


#Criando lista de números até saída
"""lista = []


while True:
    x = float(input("Digite os números a serem somados (0 = sair): "))
    if x == 0:
        break
    else:
        lista.append(x)
for i in lista:
    print(i)

Em Java:    for(int i = 0, i < 10, i+=2)
Em Python:  for i in range(0, 10, 2)
ou :        i = 0
            while i < 10:
                i+=2

"""
