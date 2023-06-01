import os  
from datetime import datetime 
class Conta:
    def __init__(self,nome, ag, num, lim):
        self.nome = nome
        self.saldo = 0
        self.agencia = ag
        self.numero = num
        self.limite = lim
        self.extrato = "Extrato da Conta: {}\nDono: {}".format(self.numero,self.nome)

    def imprimir_extrato(self):
        print(self.extrato)
        print("Saldo: ", self.saldo)

    def deposito(self):
        data_hora_atual = datetime.now().replace(microsecond=0)
        valor = float(input("Valor que deseja depositar: "))
        self.saldo += valor
        mensagem = "{}\nDepósito de {}\n".format(data_hora_atual.strftime("%d-%m-%Y %H:%M:%S"),valor)
        self.extrato += mensagem
        print("Depósito de ", valor," realizado com sucesso!")

    def saque(self):
        data_hora_atual = datetime.now().replace(microsecond=0)
        valor = float(input("Valor que deseja sacar: "))
        if self.saldo >= valor:
            self.saldo -= valor
            mensagem = "{}\nSaque de {}\n".format(data_hora_atual.strftime("%d-%m-%Y %H:%M:%S"),valor)
            self.extrato += mensagem
            print("Saque de ", valor," realizado com sucesso!")
        else:
            print("Saldo insuficiente")
    def pix(self,conta2):
        data_hora_atual = datetime.now().replace(microsecond=0)
        valor = float(input("Valor a ser enviado para {}: ".format(conta2.nome)))
        if self.saldo >= valor:
            self.saldo -= valor
            conta2.saldo += valor
            mensagem = "{}\nPix de {} para {}\n".format(data_hora_atual.strftime("%d-%m-%Y %H:%M:%S"),valor,conta2.nome)
            self.extrato += mensagem
            mensagem = "{}\nPix de {} recebido por {}\n".format(data_hora_atual.strftime("%d-%m-%Y %H:%M:%S"),valor,self.nome)
            conta2.extrato += mensagem
            print("Saque de ", valor," realizado com sucesso!")
        else:
            print("Saldo insuficiente")
            
c1 = Conta("Gustavo","123-4", "200",1000)
c2 = Conta("TK","123-4", "300",1000)
c3 = Conta("Clediomar","123-4", "400",1000)
c4 = Conta("Marças", "123-4","100",1000)
acessar = "s"
BdD = [c1,c2,c3,c4]
while True:
    op = int(input("Digite uma opção:\n0. Sair\n1. Extrato\n2. Deposito\n3. Saque\n4. Pix\n"))
    if op == 0:
        break
    elif op == 1:
        c1.imprimir_extrato()
    elif op == 2:
        c1.deposito()
    elif op == 3:
        c1.saque()
    elif op == 4:
        num = input("Número da conta que deseja enviar o pix: ")
        for indice, element in enumerate(BdD):
            if element.numero == num:
                destinatario = element
                c1.pix(destinatario)
                break
            elif indice == len(BdD):
                print("Este número não está atribuído a uma conta")
    os.system("pause")
    os.system("cls")
