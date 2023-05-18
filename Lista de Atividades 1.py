
#Faça um algoritmo que leia os valores A,B,C e imprima na tela se a a soma de A+B é menor que C
def algoritmo(A,B,C):
    if(C>(A+B)):
        print(str(C) + " é maior que a soma de " + str(A) + " + " + str(B))
    else:
        print(str(C) + " é menor que a soma de " + str(A) + " + " + str(B))
algoritmo(1,2,10)

#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprima o resultado
def algoritmo2(A):
    if(A>=0):
        print(A*2)
    else:
        print(A*3)
algoritmo2(-1)

#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as segintes fórmulas:
#-Para Homens: (72.7 * h) - 58
#-Para Mulheres : (62.1 * h) - 44.7
def Pesoideal(altura,sexo):
    Peso_ideal = 0
    if(sexo == 'M'):
       Peso_ideal = (72.7 * altura) - 58
    else:
        Peso_ideal = (62.1 * altura) - 44.7
    return Peso_ideal
print(Pesoideal(180,'M'))

#Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de aproveitamento, usando a fórmula: MA = Nota1 + nota2 * 2 + nota3 * 3 + ME)/7
def algoritmo3(Identificacao, nota1,nota2,nota3, ME):
    MA = (nota1 + nota2 * 2 + nota3 * 3 + ME)/7
    return MA

#Construa um algoritmo em portugol, que receba três valores, A, B e C, e armazene-os em três variáveis com os seguntes nomes: MAIOR, INTER e MENOR
def Maior_Inter_Menor(A,B,C):
    MAIOR = 0
    INT = 0
    MENOR = 0
    if(A>B):
        if(B>C):
            MAIOR = A
            INT = B
            MENOR = C
        else:
            if(A<C):
                MAIOR = C
                INT = A
                MENOR = B
            else:
                MAIOR = A
                INT = C
                MENOR = B
    if(A<B):
        if(B>C):
            MAIOR = B
            INT = C
            MENOR = A
        else:
            if(A>C):
                MAIOR = B
                INT = A
                MENOR = C
            else:
                MAIOR = C
                INT = B
                MENOR = A
    print("Maior: " + str(MAIOR) + "\nINTER: " + str(INT) + "\nMENOR: " + str(MENOR))
Maior_Inter_Menor(7,1,20)
# ou 
def Maior_Inter_Menor_Array():
    tamanho = 3
    lista = []
    for i in range(tamanho):
        elemento = input("Digite o elemento {}: ".format(i+1))
        lista.append(elemento)
    lista.sort(reverse=1)
    print("Maior: " + str(lista[0]) + "\nINTER: " + str(lista[1]) + "\nMENOR: " + str(lista[2]))
Maior_Inter_Menor_Array()

    