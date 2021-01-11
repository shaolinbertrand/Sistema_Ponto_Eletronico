from datetime import datetime
from tkinter import *

def database():

    arquivo = open("usuarios.txt","r")
    usuarios = arquivo.readlines()
    for index in range(len(usuarios)):
        usuarios[index] = usuarios[index].rstrip('\n')
    arquivo2 = open("senhas.txt","r")
    senhas = arquivo2.readlines()
    for index in range(len(senhas)):
        senhas[index] = senhas[index].rstrip('\n')
    print(usuarios)
    print(senhas)
    print (entradaUsuario.get())
    if entradaUsuario.get() in usuarios and entradaSenha.get() in senhas:
            print ("entrou")
            resultado['text'] = 'Registro Realizado!'
            resultado['fg'] = 'blue'
            data_e_hora_atuais = datetime.now()
            arquivo3 = open("ponto de controle.txt", "a")
            data_e_hora_em_texto = data_e_hora_atuais.strftime(entradaUsuario.get()+' Registro %d/%m/%Y %H:%M\n')
            arquivo3.write(data_e_hora_em_texto)

            
    if entradaSenha.get() not in senhas and entradaUsuario.get() in usuarios:
             resultado['text'] = 'Senha inválido!'
             resultado['fg'] = 'red'
             
    if entradaUsuario.get() not in usuarios and entradaSenha.get() in senhas:
            resultado['text'] = 'Usuário inválido'
            resultado['fg'] = 'red'
            
    if entradaUsuario.get() not in usuarios and entradaSenha.get() not in senhas:
        resultado['text'] = 'Usuário e Senha inválidos'
        resultado['fg'] = 'red'

    arquivo.close()
    arquivo2.close()
 
win_width, win_height = 350, 100
i = Tk()
i.geometry('{}x{}'.format(win_width,win_height))
i.title('Ponto Eletronico')

msgUsuario = Label(i, wraplength=win_width,text = 'Usuário')
msgUsuario.pack()

entradaUsuario = Entry(i,cursor="hand2",width=30)
entradaUsuario.pack()

msgSenha = Label(i, wraplength=win_width, text = 'Senha')
msgSenha.pack()

entradaSenha = Entry(i,show="*",cursor="hand2",width=30)
entradaSenha.pack()

botãoLogin = Button(i, text = 'Entrar', command = database)
botãoLogin.pack()

resultado = Label(i, text = "")
resultado.pack()
i.mainloop()