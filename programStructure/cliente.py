import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

#HOST = '200.239.165.217'
HOST = 'localhost'
PORT = 8000


class Cliente:
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))

        #login = tkinter.Tk()
        #login.withdraw()

        #self.apelido = simpledialog.askstring("O Mensageiro", "Escolha um apelido", parent=login) #initialvalue="Apelido")
        #self.senha = simpledialog.askstring("O Mensageiro", "Escolha uma senha", parent=login)
        #self.igu_feito = False
        #self.rodando = True

        igu_thread = threading.Thread(target=self.igu_loop)
        receive_thread = threading.Thread(target=self.receive)

        igu_thread.start()
        receive_thread.start()

    def igu_loop(self):

        self.janela = tkinter.Tk()
        self.janela.title("O Mensageiro")
        self.janela['bg'] = "lightgrey"

        self.chat_label = tkinter.Label(self.janela, text='Chat:', bg='lightgrey')
        self.chat_label.config(font=('Arial', 12))
        self.chat_label.pack(padx=20, pady=5)

        self.area_texto = tkinter.scrolledtext.ScrolledText(self.janela)
        self.area_texto.pack(padx=20, pady=5)
        self.area_texto.config(state='disabled')

        self.msg_label = tkinter.Label(self.janela, text='Mensagem:', bg='lightgrey')
        self.msg_label.config(font=('Arial', 12))
        self.msg_label.pack(padx=20, pady=5)

        self.area_input = tkinter.Text(self.janela, height=3)
        self.area_input.pack(padx=20, pady=5)

        self.botao_enviar = tkinter.Button(self.janela, text='Enviar', command=self.write)
        self.botao_enviar.config(font=('Arial', 12))
        self.botao_enviar.pack(padx=20, pady=5)

        self.igu_feito = True

        self.janela.protocol("WM_DELETE_WINDOW", self.parar)

        self.janela.mainloop()

    def write(self):
        mensagem = f"{self.apelido}: {self.area_input.get('1.0', 'end')}"
        self.s.send(mensagem.encode('utf-8'))
        self.area_input.delete('1.0', 'end')

    def parar(self):
        self.rodando = False
        self.janela.destroy()
        self.s.close()
        exit(0)

    def receive(self):
        while self.rodando:
            try:
                mensagem = self.s.recv(1024).decode('utf-8')
                if mensagem == 'APELIDO':
                    self.s.send(self.apelido.encode('utf-8'))
                elif mensagem == 'SENHA':
                    self.s.send(self.senha.encode('utf-8'))
                elif mensagem == 'WRONG':
                    self.parar()
                else:
                    if self.igu_feito:
                        self.area_texto.config(state='normal')
                        self.area_texto.insert('end', mensagem)
                        self.area_texto.yview('end') # Rolamento sempre para baixo
                        self.area_texto.config(state='disable')

            except ConnectionAbortedError:
                break
            except:
                print('ERROR')
                self.s.close()
                break


