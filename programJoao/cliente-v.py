import socket
import sys
import threading
from tkinter import *

import tkinter.scrolledtext
from tkinter import simpledialog
from GradientFrame import GradientFrame


HOST = '200.239.165.217'
PORT = 8000

class Cliente:
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))

        login = Tk()
        login.withdraw()

        self.apelido = simpledialog.askstring("Apelido", "Digite seu login", parent=login)
        self.senha = simpledialog.askstring("Senha", "Digite sua senha", parent=login)

        self.igu_feito = False
        self.rodando = True

        igu_thread = threading.Thread(target=self.igu_loop)
        receive_thread = threading.Thread(target=self.receive)

        igu_thread.start()
        receive_thread.start()

    def igu_loop(self):

        self.janela = Tk()
        self.janela.title('O Mensageiro')
        
        self.janela.geometry("1366x768")
        self.janela['bg'] = "light cyan"
        
        self.quadro=Frame(self.janela,bg='white')
        self.rolagem = Scrollbar(self.quadro, orient=VERTICAL,bg='white') 
        
        self.listagem = Listbox(self.quadro,width=78,height=20, yscrollcommand=self.rolagem.set,font=('times',13))   
        self.rolagem.config(command=self.listagem.yview) #
        self.rolagem.pack(side=RIGHT, fill=Y)#
        self.listagem.pack(pady=15) 
        self.quadro.pack()
        
        self.entry1 = Text(self.janela, height=3)
        self.entry1.pack(padx=20, pady=5)        
     
        self.button1 = Button(self.janela,text='Enviar mensagem',command=self.write) 
        self.button1.pack(padx=20, pady=5)     
        
        self.lista=['😀','😄','😉','😂','😇','😍','😗','😝','😢','😠','😡','😰','😵','😴']

        x=50
        
        
        self.title = Label(self.janela, font=("Arial", 15),  text = "Bem vindo: " + self.apelido ,bg='white').place(x = 1020,y=100)


        gf = GradientFrame(self.janela, colors = ("white", "light cyan"), width = 1366, height = 65)
        gf.config(direction = gf.top2bottom)
        gf.pack()                     
        
        self.e1 = Button(self.janela,text=self.lista[0],command=lambda:self.entry1.insert('end', self.lista[0]),bg = "white") 
        self.e1.config(font=('Arial', 15))
        self.e1.place(x=320, y=520)
        
        self.e2 = Button(self.janela,text=self.lista[1],command=lambda:self.entry1.insert('end', self.lista[1]),bg = "white") 
        self.e2.config(font=('Arial', 15))
        self.e2.place(x=320+x, y=520)
               
        self.e3 = Button(self.janela,text=self.lista[2],command=lambda:self.entry1.insert('end', self.lista[2]),bg = "white") 
        self.e3.config(font=('Arial', 15))
        self.e3.place(x=320+x*2, y=520)
             
        self.e4= Button(self.janela,text=self.lista[3],command=lambda:self.entry1.insert('end', self.lista[3]),bg = "white") 
        self.e4.config(font=('Arial', 15))
        self.e4.place(x=320+x*3, y=520)
                     
        self.e5 = Button(self.janela,text=self.lista[4],command=lambda:self.entry1.insert('end', self.lista[4]),bg = "white") 
        self.e5.config(font=('Arial', 15))
        self.e5.place(x=320+x*3, y=520)
                     
        self.e6 = Button(self.janela,text=self.lista[5],command=lambda:self.entry1.insert('end', self.lista[5]),bg = "white") 
        self.e6.config(font=('Arial', 15))
        self.e6.place(x=320+x*4, y=520)

        self.e7 = Button(self.janela,text=self.lista[6],command=lambda:self.entry1.insert('end', self.lista[6]),bg = "white") 
        self.e7.config(font=('Arial', 15))
        self.e7.place(x=320+x*5, y=520)
             
        self.e8 = Button(self.janela,text=self.lista[7],command=lambda:self.entry1.insert('end', self.lista[7]),bg = "white") 
        self.e8.config(font=('Arial', 15))
        self.e8.place(x=320+x*6, y=520)
        
        self.e9 = Button(self.janela,text=self.lista[8],command=lambda:self.entry1.insert('end', self.lista[8]),bg = "white") 
        self.e9.config(font=('Arial', 15))
        self.e9.place(x=320+x*7, y=520)

        self.e10 = Button(self.janela,text=self.lista[9],command=lambda:self.entry1.insert('end', self.lista[9]),bg = "white") 
        self.e10.config(font=('Arial', 15))
        self.e10.place(x=320+x*8, y=520)
 
        self.e11 = Button(self.janela,text=self.lista[10],command=lambda:self.entry1.insert('end', self.lista[10]),bg = "white") 
        self.e11.config(font=('Arial', 15))
        self.e11.place(x=320+x*9, y=520)
                
 
        self.e12 = Button(self.janela,text=self.lista[11],command=lambda:self.entry1.insert('end', self.lista[11]),bg = "white") 
        self.e12.config(font=('Arial', 15))
        self.e12.place(x=320+x*10, y=520)
                 
  
        self.e13 = Button(self.janela,text=self.lista[12],command=lambda:self.entry1.insert('end', self.lista[12]),bg = "white") 
        self.e13.config(font=('Arial', 15))
        self.e13.place(x=320+x*11, y=520)
                    
        self.e14 = Button(self.janela,text=self.lista[13],command=lambda:self.entry1.insert('end', self.lista[13]),bg = "white") 
        self.e14.config(font=('Arial', 15))
        self.e14.place(x=320+x*12, y=520)
        

        self.igu_feito = True
        self.janela.protocol("WM_DELETE_WINDOW", self.parar)                        
        self.janela.mainloop()
        
    def write(self):
        mensagem = f"{self.apelido}: {self.entry1.get('1.0', 'end')}"
        self.s.send(mensagem.encode('utf-8'))
        self.entry1.delete('1.0', 'end')
       

    def parar(self):
        saida = f"{self.apelido}: saiu do chat"
        self.s.send(saida.encode('utf-8'))

        self.rodando = False
        self.janela.destroy()
        self.s.close()
        sys.exit()
        print('FECHADA')

    def receive(self):
        while self.rodando:
            try:
                mensagem = str(self.s.recv(1024).decode('utf-8'))
                msg = mensagem.rstrip('\n')
                print(mensagem)
                if mensagem == 'APELIDO':
                    self.s.send(self.apelido.encode('utf-8'))
                elif mensagem== 'SENHA':
                    self.s.send(self.senha.encode('utf-8'))

                else:
                    if self.igu_feito:
                    
                        self.listagem.insert('end',mensagem.strip())
                        #self.listagem.insert(END,(mensagem))
                        #index = self.listagem.get(0, "end").index(mensagem.strip())
                        #print(index)
                        #print(mensagem)
                        #men=self.listagem.Items[index].ToString()
                        #print(self.apelido)
                            
                        #self.listagem.insert('end',mensagem.strip())
                        #self.rolagem.yview('end') # Rolamento sempre para baixo
                        #mensagem=str(mensagem)
                        #print(mensagem)
                        
                  
                         #self.listagem.insert('end',mensagem.strip())
                        #index = self.listagem.get(0, "end").index(mensagem.strip())

                    
                            #self.listagem.insert('end',mensagem.strip())
                            #index = self.listagem.get(0, "end").index(mensagem.strip())
                            
                            #self.listagem.insert('end',mensagem.strip())
                            #self.listagem.itemconfig(index, {'fg': 'blue'})
                        
                        
            except ConnectionAbortedError:
                break
            except:
                print('ERROR')
                self.s.close()
                break

cliente = Cliente(HOST, PORT)