class Calculadora:
    n1 = 0
    n2 = 0

    def soma(self):
        self.n1 = float(input("Digite a Parcela 1: "))
        self.n2 = float(input("Digite a Parcela 2: "))
        print("Soma: {:.2f}".format(self.n1+self.n2))
        return self.n1+self.n2
    def subtracao(self):
        self.n1 = float(input("Digite o Minuendo: "))
        self.n2 = float(input("Digite o Subtraendo: "))
        print("Diferença: {:.2f}".format(self.n1-self.n2))
        return self.n1-self.n2
    def divisao(self):
        self.n1 = float(input("Digite o Dividendo: "))
        self.n2 = float(input("Digite o Divisor: "))
        if self.n2 == 0:
            print("Impossivel dividir por 0!")
            return None
        else:
            Q = int(self.n1/self.n2)
            print("Quociente: {}\nResto: {}".format(Q,self.n1-(self.n2*Q)))
        return Q
    def multiplicacao(self):
        self.n1 = float(input("Digite o Produto 1: "))
        self.n2 = float(input("Digite o Produto 2: "))
        print("Produto: {:.2f}".format(self.n1*self.n2))
        return self.n1*self.n2
    def radiciacao(self):
        self.n1 = float(input("Digite o Radicando: "))
        self.n2 = float(input("Digite o Índice: "))
        Resultado = self.n1**(1/self.n2)
        print("Resultado: ", Resultado)
        return Resultado

    def potenciacao(self):
        self.n1 = float(input("Digite a Base: "))
        self.n2 = float(input("Digite o Expoente: "))
        Resultado = pow(self.n1,self.n2)
        print("Resultado: ", Resultado)
        return Resultado
        """ for i in range(self.n2):
            Resultado = Resultado * self.n1

            OU

            Resultado = self.n1**self.n2
        """
    
c = Calculadora()
while True:
    R = input("Oque deseja fazer?:\nA - Adição\nS - Subtração\nM - Multiplicação\nD - Divisão\nR - Radiciação\nP - Potenciação\n")
    if R == "A" or R == "a":
        c.soma()
    elif R == "S" or R == "s":
        c.subtracao()
    elif R == "M" or R == "m":
        c.multiplicacao()
    elif R == "D" or R == "d":
        c.divisao()
    elif R == "R" or R == "r":
        c.radiciacao()
    elif R == "P" or R == "p":
        c.potenciacao()
    R = input("Deseja sair do programa? [y/n]")
    if R == "Y" or R == "y":
        break