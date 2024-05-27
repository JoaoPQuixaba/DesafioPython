import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3

connection = sqlite3.connect("teste.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado TEXT)")

def VerificarCPF(CPF):
    for trecho in CPF.split("."):
        if len(trecho) != 3:
            return False
    return True

def inserevalores(nome, cpf, estado):
    cursor.execute("INSERT INTO Tabela1 (nome, cpf, estado) VALUES (?, ?, ?)", (nome, cpf, estado))
    connection.commit()

def pegavalores():
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def funcSalvar(nome, cpf, estado):
    if VerificarCPF(cpf):
        inserevalores(nome, cpf, estado)
        mb.showinfo("Informação", "Dados salvos com sucesso!")
    else:
        mb.showerror("Erro", "CPF inválido!")

def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)
    
    label_nome = tkinter.Label(root, text="Nome")
    label_nome.pack()

    textoEntradaNome = tkinter.StringVar()
    e1 = tkinter.Entry(root, textvariable=textoEntradaNome)
    e1.pack()

    label_cpf = tkinter.Label(root, text="CPF")
    label_cpf.pack()
    textoEntradaCPF = tkinter.StringVar()
    e_cpf = tkinter.Entry(root, textvariable=textoEntradaCPF)
    e_cpf.pack()

    label_estado = tkinter.Label(root, text="Estado")
    label_estado.pack()
    textoEntradaEstado = tkinter.StringVar()
    e_estado = tkinter.Entry(root, textvariable=textoEntradaEstado)
    e_estado.pack()
    
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = lambda: funcSalvar(textoEntradaNome.get(), textoEntradaCPF.get(), textoEntradaEstado.get())
    test2.pack()

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

Main()
