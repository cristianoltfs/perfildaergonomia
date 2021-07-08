import socket
import threading
import select

def conecta( conn, ender ):
    print('Cliente {} recebido.'.format( ender ))
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.connect( (ender[0], ender[1]) )

HOST = "200.239.165.217"
PORT = 13333
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket ok!")
s.bind((HOST,PORT))
print("Bind ok!")
s.listen()
print('Listen ok!')
print('Aguardando conexão de um cliente')
while True:
    conn, ender = s.accept()
    print('Conectado em ip: ', ender[0])
    print('Conectado em port: ', ender[1])
    threading.Thread( target = conecta, args = ( conn, ender ) ).start()