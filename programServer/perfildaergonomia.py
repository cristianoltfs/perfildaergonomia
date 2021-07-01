#!/usr/bin/env python3

import socket

# HOST = '200.239.167.212'
HOST = 'localhost'
PORT = 13333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando conexão de um cliente')
conn, ender = s.accept()

print('Conectado em: ', ender)

n = 0

while True:
    data = conn.recv(1024)
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data)
