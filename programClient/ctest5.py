import socket

HOST = '200.239.165.217'
PORT = 13333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

nome = input()
s.sendall(str.encode(nome))

while True:

    servmsn =  s.recv(1024)
    print("Resposta do servidor:" ,servmsn.decode())

    nome = input()
    
    if nome == 'sair':
        break

s.close