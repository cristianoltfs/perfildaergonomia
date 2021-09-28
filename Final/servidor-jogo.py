import socket
import threading
import pandas as pd
from random import sample
import _pickle as cPickle

HOST = '200.239.165.217'
PORT = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
clientes = []
apelidos = []
dic = {}
sorteio = sample(range(0, 108), 108)

def transmitir_mensagem(mensagem):
    for cliente in clientes:
        print('mensagem pública')
        cliente.send(mensagem)
            
def cabo_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            transmitir_mensagem(mensagem)
            mensagem = mensagem.decode('utf-8')
        except:
            indice = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            apelido = apelidos[indice]
            apelidos.remove(apelido)
            break

def receber_cliente():
    while True:
        cliente, endereco = s.accept()
        clientes.append(cliente)
        t = threading.Thread(target=cabo_cliente, args=(cliente,))
        t.start()        
        
print("Servidor rodando...")
receber_cliente() 

