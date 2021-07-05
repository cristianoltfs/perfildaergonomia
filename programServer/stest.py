#!/usr/bin/env python3

# script que age como um servidor
# fica esperando, escutando e aceitando conexões

import socket

# socket é a combinação de um ip com um número de porta

HOST = 'localhost'
# HOST = '200.239.167.212'
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
# conn, ender = s.accept()

dic = {'nome':'', 'ip':'', 'port':''}

while True:
    conn, ender = s.accept()
    print('Conectado em ip: ', ender[0])
    print('Conectado em port: ', ender[1])

    # 1024 bytes - tamanho máximo de dados recebidos nessa conexão
    msg = conn.recv(1024)
    print('Player : ', msg.decode())

    if  not ((msg.decode() in dic['nome']) and (ender[0] in dic['ip']) and (ender[1] in dic['port'])):
        dic = {'nome':msg.decode(), 'ip':ender[0], 'port':ender[1]}
        print(dic)
        print('teste')
    else:
        print('já está jogando')
    if not msg:
        ('Fechando a conexão')
        conn.close()
        break

    #enviar mensagem de volta para o cliente
    conn.sendall(msg)
