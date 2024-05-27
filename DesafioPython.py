import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3
import re

connection = sqlite3.connect("teste.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado TEXT, tipo TEXT)")

def VerificarCPF(CPF):
    pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    if pattern.match(CPF):
        return True
    else:
        return False

def inserevalores(nome, cpf, estado, tipo):
    cursor.execute("INSERT INTO Tabela1 (nome, cpf, estado, tipo) VALUES (?, ?, ?, ?)", (nome, cpf, estado, tipo))
    connection.commit()

def pegavalores():
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def funcSalvar(nome, cpf, estado, tipo):
    if VerificarCPF(cpf):
        inserevalores(nome, cpf, estado, tipo)
        mb.showinfo("Informação", "Dados salvos com sucesso!")
    else:
        mb.showerror("Erro", "CPF inválido! Formato correto: 111.111.111-11")

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

    label_tipo = tkinter.Label(root, text="Tipo")
    label_tipo.pack()
    tipo_var = tkinter.StringVar()
    combobox_tipo = ttk.Combobox(root, textvariable=tipo_var)
    combobox_tipo['values'] = ("CLR", "MEI", "SÓCiO")
    combobox_tipo.pack()
    
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = lambda: funcSalvar(textoEntradaNome.get(), textoEntradaCPF.get(), textoEntradaEstado.get(), tipo_var.get())
    test2.pack()

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

Main()
