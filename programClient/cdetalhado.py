#!/usr/bin/env python3

import socket

HOST = '200.239.165.217'
PORT = 17000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# pedir conexão no socket no servidor
s.connect((HOST, PORT))


while True:
    # enviar uma mensagem ao servidor
    print('Digite seu nome:')
    nome = input()
    if nome == 'sair' or nome == '':
        break
    s.sendall(str.encode(nome))

    # pegando a resposta do servidor
    #msgServer = s.recv(1024)
    #print(msgServer.decode(), 'Mensagem que enviou!')