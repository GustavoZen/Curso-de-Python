from tkinter import *
from LdFA import *
from ClassJanela_10 import *

bg="#F8F1F1"
fg="#025464"

carrinho = []
total = None

def addCart():
    global total
    conn = conexaoBanco("produtos.db")
    itemSelecionado = tv.focus()
    quantidade = float(entQtd.get())
    existe = False
    if itemSelecionado:
        valores = tv.item(itemSelecionado)['values']
        produto = valores[1]
        for element in carrinho:
            if produto == element[0]:
                element[2] += float(quantidade)
                existe = True
        if not existe:
            carrinho.append([produto,valores[2],quantidade])
    attTotal()
    conn.close()
    
def attTotal():
    total = 0
    carrinhoHUD.delete(*carrinhoHUD.get_children())
    for row in carrinho:
        carrinhoHUD.insert('', 'end', values=row)
        total += float(row[1]) * float(row[2])  # Calcula o preço total
    lbTotal['text'] = f"Total: R$ {total:.2f}"

def delCart():
    global total
    itemSelecionado = carrinhoHUD.focus()
    quantidade = float(entQtd.get())
    if itemSelecionado:
        valores = carrinhoHUD.item(itemSelecionado)['values']
        produto = valores[0]
        for index,element in enumerate(carrinho):
            if produto == element[0]:
                element[2] -= float(quantidade)
            if element[2] == 0:
                carrinho.remove(carrinho[index])
    attTotal()
    
comprasJanela = ClassJanela("Compras",800,500,bg)
conn = conexaoBanco("estoque.db")
cursor = conn.cursor()
cursor.execute('SELECT id, nome, preço FROM produtos')
total = 0

lb1 = Label(comprasJanela.janela,text="Produtos Disponíveis: ",fg=fg,bg=bg)
lb1.grid(column=0,row=0)
tv = ttk.Treeview(comprasJanela.janela,columns=('id','produto','preco'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('produto',minwidth=0,width=150)
tv.column('preco',minwidth=0,width=100)
tv.heading('id',text="ID")
tv.heading('produto',text="PRODUTO")
tv.heading('preco',text="PREÇO")
tv.grid(column=0,row=1,columnspan=3,padx=10,pady=10)
for row in cursor.fetchall():
    tv.insert('', 'end', values=row)

lbTotal = Label(comprasJanela.janela,fg=fg,bg=bg)
lbTotal.place(x=450,y=255)

lbQtd = Label(comprasJanela.janela,text="Quantidade: ",bg=bg,fg=fg)
lbQtd.place(x=350,y=25)
entQtd = Entry(comprasJanela.janela)
entQtd.place(x=320,y=45)

carrinhoHUD = ttk.Treeview(comprasJanela.janela, columns=('produto', 'preco', 'qtd'),show="headings")
carrinhoHUD.column('produto', minwidth=0, width=150)
carrinhoHUD.column('preco', minwidth=0, width=100)
carrinhoHUD.column('qtd', minwidth=0, width=50)
carrinhoHUD.heading('produto', text="PRODUTO")
carrinhoHUD.heading('preco', text="PREÇO")
carrinhoHUD.heading('qtd', text="QTD")
carrinhoHUD.place(x=450, y=30)
for row in carrinho:
    carrinhoHUD.insert('','end',values = row)

btnAddCart = Button(comprasJanela.janela,text="Adicionar ao Carrinho",command=lambda:addCart())
btnAddCart.place(x=320,y=70)

btnDelCart = Button(comprasJanela.janela,text="Retirar do Carrinho",command=lambda:delCart())
btnDelCart.place(x=320,y=100)

comprasJanela.janela.protocol("WM_DELETE_WINDOW", comprasJanela.janela.withdraw)