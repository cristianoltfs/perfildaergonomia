import socket

HOST = '200.239.165.217'
PORT = 13333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Digite seu nome:')
nome = input()
s.sendall(str.encode(nome))

print('Digite a sua sala:')
sala = input()
s.sendall(str.encode(sala))

while True:

    servmsn =  s.recv(1024)
    print("Resposta do servidor:" ,servmsn.decode())

    nome = input()

    if nome == 'sair':
        s.sendall(str.encode(nome))
        break

    s.sendall(str.encode(nome))


s.close