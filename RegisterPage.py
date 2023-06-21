from tkinter import *
from LdFA import *
from tkinter import ttk
from sqlite3 import Error
from ClassJanela_10 import *

bg="#F8F1F1"
fg="#025464"

def edit():
    item_selecionado = tv.focus()
    if item_selecionado:
        valores = tv.item(item_selecionado)['values']

        idSelecionado = valores[0]
        produtoSelecionado = valores[1]
        quantidadeSelecionada = valores[2]
        precoSelecionado = valores[3]
        entId.insert(0,idSelecionado)
        entProduto.insert(0,produtoSelecionado)
        entQuantidade.insert(0,quantidadeSelecionada)
        entPreco.insert(0,precoSelecionado)

def atualizarTreeView():
    tv.delete(*tv.get_children())

    cursor.execute('SELECT id, nome, qtd, preço, tipo FROM produtos')

    for row in cursor.fetchall():
        tv.insert('', 'end', values=row)

def add():
    conn = conexaoBanco("estoque.db")
    cursor = conn.cursor()
    nome = entProduto.get()
    quantidade = entQuantidade.get()
    preco = entPreco.get()
    tipo = vtipo.get()
    if nome != "" and quantidade != "":
        try:
            cursor.execute('INSERT INTO produtos (nome, qtd, preço, tipo) VALUES (?, ?, ?, ?)',(nome,quantidade,preco,tipo))
            conn.commit()
        except Error as ex:
            print(ex)
        finally:
            atualizarTreeView()
            conn.close()
    
def att():
    conn = conexaoBanco("estoque.db")
    cursor = conn.cursor()
    id = entId.get()
    nome = entProduto.get()
    quantidade = entQuantidade.get()
    preco = entPreco.get()
    tipo = vtipo.get()
    try:
        cursor.execute('UPDATE produtos SET nome = ?, qtd = ?, preço = ?, tipo = ? WHERE id = ?',(nome,quantidade,preco,tipo,id))
        conn.commit()
    except Error as ex:
            print(ex)
    finally:
            atualizarTreeView()
            conn.close()

def delete():
    conn = conexaoBanco("estoque.db")
    cursor = conn.cursor()
    item_selecionado = tv.focus()
    if item_selecionado:
        valores = tv.item(item_selecionado)['values']
        id_selecionado = valores[0]
    try:
        cursor.execute('DELETE FROM produtos WHERE id = ?', (id_selecionado,))
        conn.commit()
    except Error as ex:
        print(ex)
    finally:
        atualizarTreeView()
        conn.close

registerPage = ClassJanela("Registro de Produtos",600,400,bg)
conn = conexaoBanco("estoque.db")
cursor = conn.cursor()
cursor.execute('SELECT id, nome, qtd, preço, tipo FROM produtos')
lbId = Label(registerPage.janela,text="ID:",fg=fg,bg=bg)
lbId.grid(column=0,row=0)
entId = Entry(registerPage.janela)
entId.grid(column=0,row=1)

lbProduto = Label(registerPage.janela,text="Produto: ",fg=fg,bg=bg)
lbProduto.grid(column=1,row=0,padx=5)
entProduto = Entry(registerPage.janela)
entProduto.grid(column=1,row=1,padx=5)

lbQuantidade = Label(registerPage.janela,text="Quantidade:",fg=fg,bg=bg)
lbQuantidade.grid(column=2,row=0)
entQuantidade = Entry(registerPage.janela)
entQuantidade.grid(column=2,row=1)

lbPreco = Label(registerPage.janela,text="Preço:",fg=fg,bg=bg)
lbPreco.place(x=440,y=0)
entPreco = Entry(registerPage.janela)
entPreco.place(x=400,y=24)

vtipo = StringVar()
vtipo.set("P")
cbtipo = Checkbutton(text="Perecível",variable=vtipo,onvalue="P",offvalue="N.P",bg=bg)
cbtipo.place(x=520,y=20)

tv = ttk.Treeview(registerPage.janela,columns=('id','produto','qtd','preco','tipo'),show='headings')
tv.column('id',minwidth=0,width=25)
tv.column('produto',minwidth=0,width=150)
tv.column('qtd',minwidth=0,width=100)
tv.column('preco',minwidth=0,width=50)
tv.column('tipo',minwidth=0,width=50)
tv.heading('id',text="ID")
tv.heading('produto',text="PRODUTO")
tv.heading('qtd',text="QUANTIDADE")
tv.heading('preco',text="Preço")
tv.heading('tipo',text="Tipo")
for row in cursor.fetchall():
    tv.insert('', 'end', values=row)

tv.grid(column=0,row=3,columnspan=3,pady=5)

btnEdit = Button(registerPage.janela,text="Editar",command=lambda:edit())
btnEdit.grid(column=0,row=4)
btnAdd = Button(registerPage.janela,text="Adicionar",command=lambda:add())
btnAdd.grid(column=1,row=4)
btnRetirar = Button(registerPage.janela,text="Retirar",command=lambda:delete())
btnRetirar.grid(column=3,row=4)
btnAtt = Button(registerPage.janela,text="Atualizar",command=lambda:att())
btnAtt.grid(column=2,row=4)

registerPage.janela.protocol("WM_DELETE_WINDOW", registerPage.janela.withdraw)