#!/usr/bin/env python3

# script que age como um servidor
# fica esperando, escutando e aceitando conexões

import socket

# socket é a combinação de um ip com um número de porta

HOST = '200.239.167.212'
PORT = 13333

# combinar HOST e PORT para montar o socket

# invocar o método socket do objeto socket
# passar como parâmetro família de protocolo e o tipo de protocolo
# IPV4 = AF_INET
# TCP = SOCK_STREAM
# criar o objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Passar os valores que serão vinculados, servido e porta
# invoca o método bind
s.bind((HOST,PORT))

# colocar em modo de escuta no servidor
s.listen()
print('Aguardando conexão de um cliente')

# aceitar a conexão quando chegar
# crirar dois elementos: conexão e endereço
# retorno do comando s.accept (conexão e endereço)
# (comando para aceitar conexão)
conn, ender = s.accept()

print('Conectado em:', ender)

while True:
    # 1024 bytes - tamanho máximo de dados recebidos nessa conexão
    data = conn.recv(1024)
    if not data:
        ('Fechando a conexão')
        conn.close()
        break
    #enviar mensagem de volta para o cliente
    conn.sendall(data)


































