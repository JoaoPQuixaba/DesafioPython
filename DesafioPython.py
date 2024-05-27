import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import requests
from io import BytesIO

connection = sqlite3.connect("teste.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, curso TEXT, matricula INTEGER)")

def VerificarCPF(CPF):
    for trecho in CPF.split("."):
        if len(trecho) != 3:
            return False
    return True

def inserevalores(Valor1, Valor2):
    cursor.execute("INSERT INTO Tabela1 VALUES ('" + Valor1 + "', '" + Valor2 + "')")

def pegavalores():
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def funcExemplo():
    print("Exemplo de funcao")

def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)
    
    url = "https://d37iydjzbdkvr9.cloudfront.net/lista10/lista_as-dez-universidades-mais-bonitas-do-mundo/stanford-credito-stanford-edu.jpg"
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)

    img_label = tkinter.Label(root, image=photo)
    img_label.image = photo
    img_label.pack()

    label_nome = tkinter.Label(root, text="Nome")
    label_nome.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x: textoEntrada.set(e1.get() + x.char))
    e1.pack()

    label_cpf = tkinter.Label(root, text="CPF")
    label_cpf.pack()
    e_cpf = tkinter.Entry(root)
    e_cpf.pack()

    label_estado = tkinter.Label(root, text="Estado")
    label_estado.pack()
    e_estado = tkinter.Entry(root)
    e_estado.pack()
    
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = funcExemplo
    test2.pack()

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

Main()
