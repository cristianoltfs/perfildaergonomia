import socket
import threading

HOST = '200.239.165.217'
PORT = 13333

class Server (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.socket = None
    def run(self):
        self.isRunning = True
        while self.isRunning:
            if self.socket != None:
                servmsn = self.socket.recv(2048) # esperando por ate 2048 bytes...
                messageType, messageBody = servmsn.decode()


server = Server()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Digite seu nome:')
nome = input()
s.sendall(str.encode(nome))

print('Digite a sua sala:')
sala = input()
s.sendall(str.encode(sala))

server.start()


while True:

    
    servmsn =  s.recv(1024)
    print("Resposta do servidor:" ,servmsn.decode())

    nome = input()

    if nome == 'sair':
        s.sendall(str.encode(nome))
        break

    s.sendall(str.encode(nome))


s.close()