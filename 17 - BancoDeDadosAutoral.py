from RegisterPage import *
from PaginaDeCompras import *

bg="#025464"
fg="#E57C23"

def fecharJanelas():
    comprasJanela.janela.destroy()
    registerPage.janela.destroy()
    janela.destroy()

comprasJanela.janela.withdraw()
registerPage.janela.withdraw()
janela = Tk()
janela.title("Sistema")
janela.configure(width=500,height=300,bg=bg)
centralizar_janela(janela)
janela.protocol("WM_DELETE_WINDOW", fecharJanelas)

lb = Label(janela,text="SUPERMERCADO\nG.A.V",font=("Verdana",20),fg=fg,bg=bg)
lb.place(x=(500-lb.winfo_width())/4,y=(300-lb.winfo_reqheight())/2)

barra_menu = Menu(janela)
menu = Menu(barra_menu,tearoff=0)
menu.add_command(label="Compras",command=comprasJanela.janela.deiconify)
menu.add_command(label="Registrar Novos Produtos",command=registerPage.janela.deiconify)
barra_menu.add_cascade(label="Ações",menu=menu)
janela.config(menu=barra_menu)


janela.mainloop()