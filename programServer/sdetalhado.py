#!/usr/bin/env python3

# script que age como um servidor;
# fica esperando, escutando e aceitando conexões;

import socket

import threading


HOST = '200.239.165.217'
PORT = 17000

# socket é a combinação de um ip com um número de porta;
# combinar HOST e PORT para montar o socket;

# invocar o método socket do objeto socket;
# passar como parâmetro família de protocolo e o tipo de protocolo;
# IPV4 = AF_INET;
# TCP = SOCK_STREAM;
# criar o objeto socket;
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Passar os valores que serão vinculados, servidor e porta;
# invoca o método bind.
s.bind((HOST,PORT))


# essa classe vai representar o cliente dentro do servidor;
class Client(threading.Thread): # esta classe herda da classe Thread;
    def __init__(self, socket, address):
        threading.Thread.__init__(self)
        self.username = None
        self.address = address
        self.socket = socket
    
    # aqui será responsável por decodificar as mensagens de um cliente;
    def run(self):
        print('Cliente se conectou')
        
        # aqui dentro a thread vai esperar por mensagens do cliente;
        while True:
            msg = self.socket.recv(2048).decode()  # esperando por ate 2048 bytes;
            print ("Mensagem do cliente: ", msg)
            if msg == 'sair' or msg == '':
                print('Fechando conexão.')
                break
                #self.socket.close()
                #break

while True:
    # colocar em modo de escuta no servidor;
    s.listen()
    print('Aguardando conexão de um cliente.')

    # aceitar a conexão quando chegar;
    # criar dois elementos: conexão e endereço;
    # retorno do comando s.accept (conexão e endereço);
    # (comando para aceitar conexão);
    conn_cli, ender_cli = s.accept()
    print('Conectado em ip: ', ender_cli[0])
    print('Conectado em port: ', ender_cli[1])
    
    # Criar o objeto cliente;
    # instanciar o objeto cliente;
    cliente = Client(conn_cli, ender_cli)
    cliente.start() # executa o run da classe cliente;
















'''

while True:
    # receber a mensagem
    # guardar dentro da variavel msg
    msg = conn.recv(1024)
    # verificar quando terminou de receber os dados
    if msg == 'sair' or msg == '':
        print('Fechando conexão.')
        conn.close()
        break
    # Enviar de volta a mensagem para o cliente
    conn.sendall(msg)

'''