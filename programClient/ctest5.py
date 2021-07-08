import socket

HOST = '200.239.165.217'
PORT = 13333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode('Cliente conectado'))

while True:
    servmsn =  s.recv(1024)
    print("Enviada do servidor :" ,servmsn.decode())
    dados = input()
    s.sendall(str.encode(dados))
    if dados == 'sair':
        break

s.close