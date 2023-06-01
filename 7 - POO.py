#   Definindo a Classe Carro e seus atributos
class Carro:                    #[  Classe

    velmax = 150                #┍  Atributos
    vel = 0                     #|  
    ligado = False              #|
    cor = ""                    #┕
    
    def acelerar(self):         #┍  Funções
        self.vel += 10          #|
    def ligar(self):            #|
        if not self.ligado:     #|
            self.ligado = True  #|
        else:                   #| 
            print("Já ligado")  #|
    def desligar(self):         #|
        self.ligado = False     #┕
    

#   Criando objetos Carros
c1 = Carro()
c2 = Carro()
c3 = Carro()

#   Atribuindo valores ao objeto c1
c1.velmax = 200
c1.cor    = "Preto"
c1.ligado = True
c1.ligar()
c2.ligar()
c1.acelerar()
print("Velocidade: ", c1.vel)
c1.acelerar()
print("Velocidade: ", c1.vel)

#   Imprimir esses atributos
print("Velocidade Máxima: " , c1.velmax  )
print("Cor: "               , c1.cor     )
estado = "sim" if c1.ligado else "não"      #Operador Ternário
print("Ligado:"             , estado     )
