# Autor: Daniel Carvalho Gomes
# Data: 11/10/24
# Codigo: Exemplo de Interface no Tkinter

from tkinter import *

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()

    def tela(self):
        self.root.title("Cadatro FMF de Clientes")
        self.root.configure(background='orange')
        self.root.geometry('600x400')
        self.root.resizable(True, True)
        self.root.maxsize(width=1300, height=650)
        self.root.minsize(width=300, height=200)
    def frames_da_tela(self):
        self.frame_1= Frame(self.root, bd = 4,bg= '#FFFFF0',highlightbackground='#FFFFF0', highlightthickness='3')
        self.frame_1.place(relx=0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)
        self.frame_2= Frame(self.root, bd = 4,bg= '#FFFFF0',highlightbackground='#FFFFF0', highlightthickness='3')
        self.frame_2.place(relx=0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

Application()
