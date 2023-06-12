#Explicação Inicial
import LdFA
carros = [#Matriz
    ["Modelo"       , "HRV"   ],
    ["Fabricante"   , "Honda" ],
    ["Ano"          , "2016"  ],
    ["Cor"          , "Azul"  ]
    ]
linha = 0
while linha < 4:
    coluna = 0
    while coluna < 2:
        print(carros[linha][coluna], end = ",")
        coluna+=1
    print("")
    linha+=1

#somar todos os elementos de uma matriz
numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
LdFA.Printar_Matriz(numeros)
LdFA.Delay
print("Soma: {} ".format(LdFA.Somar_Matriz(numeros)))
print("Qtd de números maiores que 6: {}".format(LdFA.contar_nums_maior_que_x_na_matriz(6,numeros)))
