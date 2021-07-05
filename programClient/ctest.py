#!/usr/bin/env python3

# script que age no cliente

import socket

HOST = '200.239.167.212'
PORT = 13333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = 'Cristiano'

# pedir conexão no socket no servidor
s.connect((HOST, PORT))

# enviar uma mensagem ao servidor
s.sendall(str.encode(name))

# pegando a resposta do servidor
data = s.recv(1024)

print(data.decode(), 'você entrou no jogo!')
