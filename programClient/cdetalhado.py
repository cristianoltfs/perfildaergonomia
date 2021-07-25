#!/usr/bin/env python3

import socket

import threading


HOST = '200.239.165.217'
PORT = 17000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# pedir conexão no socket no servidor
s.connect((HOST, PORT))

# classe que represneta o servidor
class Server (threading.Thread):
    def __init__(self, socket, address):
        threading.Thread.__init__(self)
        self.username = None
        self.address = address
        self.socket = socket

    # aqui será responsável por decodificar as mensagens de um cliente;
    def run(self):
        print('Resposta do servidor')
        
        # aqui dentro a thread vai esperar por mensagens do servidor;
        while True:
            msg = self.socket.recv(2048).decode()  # esperando por ate 2048 bytes;
            print ("Mensagem do servidor: ", msg)
            if msg == 'sair' or msg == '':
                print('Fechando conexão.')
                break
                #self.socket.close()
                #break

    # pegando a resposta do servidor
    #msgServer = s.recv(1024)
    #print(msgServer.decode(), 'Mensagem que enviou!')

while True:
    # enviar uma mensagem ao servidor
    print('Digite seu nome:')
    print('Digite sair para sair.')
    nome = input()
    if nome == 'sair' or nome == '':
        break
    s.sendall(str.encode(nome))