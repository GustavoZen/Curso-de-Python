from tkinter import *

janela = Tk()
janela.title("Comprar Produtos")
janela.geometry("600x400")
janela.config(background="#2C3333")

def mostrar_resultado():
    global valor
    global nome
    global qtd
    if opcao.get() == 1:
        Total = float(valor.get()) * float(qtd.get()) * 0.9
        print("Produto Comprado: {}\nForma de Pagamento: À vista\nValor Total: {}".format(nome.get(),Total))
    elif opcao.get() == 2:
        Total = float(valor.get()) * float(qtd.get()) * 1.01
        Parcela = Total / 2
        print("Produto Comprado: {}\nForma de Pagamento: À Prazo\nValor Total: {}\nValor da Parcela: {}".format(nome.get(),Total,Parcela))

opcao=IntVar()

Label(janela,text="Produto:",bg="#2C3333",fg="#CBE4DE",anchor="w",font=("Arial",20)).place(x=10,y=10,width=110,height=20)
nome = Entry(janela)
nome.place(x=180, y=10)
Label(janela,text="Valor:",bg="#2C3333",fg="#CBE4DE",anchor="w",font=("Arial",20)).place(x=10,y=70,width=100,height=20)
valor = Entry(janela)
valor.place(x=180, y=70)
Label(janela,text="Quantidade:",bg="#2C3333",fg="#CBE4DE",anchor="w",font=("Arial",20)).place(x=10,y=130,width=200,height=20)
qtd = Entry(janela)
qtd.place(x=180, y=130)

avista = Radiobutton(janela,text="À vista",variable=opcao,value=1,bg="#2C3333",fg="#0E8388",font=("Arial",20),activebackground="#2C3333").place(x=30,y=170)
avista = Radiobutton(janela,text="À Prazo",variable=opcao,value=2,bg="#2C3333",fg="#0E8388",font=("Arial",20),activebackground="#2C3333").place(x=30,y=220)

Button(janela,text="Enviar",bg="#CBE4DE",fg="Black",command=lambda:mostrar_resultado()).place(y=270,x=250,width=100,height=50)

janela.mainloop()

