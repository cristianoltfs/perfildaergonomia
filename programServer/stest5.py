import socket
import threading

HOST = '200.239.165.217'
PORT = 13333

class Sala():
    pass

class Cliente(threading.Thread):
    def __init__(self, cli_address, cli_socket):
        threading.Thread.__init__(self)
        self.username = cli_socket.recv(1024)
        self.csocket = cli_socket
        self.caddress = cli_address
        self.sala = 0
        print ("Nova conexão. Player: ", self.username.decode(), cli_address, "Conectado")
    def run(self):
        if self.sala == 0:
            self.sala = self.csocket.recv(1024)
        self.csocket.sendall(self.username + bytes(' você está conectado na sala ','UTF-8') + self.sala)
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'sair' or msg == '':
                break
            print ("Mensagem do cliente: ", msg)
            self.csocket.sendall(bytes(msg,'UTF-8'))
        print ("Cliente ", cli_address , " desconectado!")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
print("Servidor inicializado!")
print("Esperando conxão de clientes!")

while True:
    s.listen()
    cli_socket, cli_address = s.accept()
    cliente = Cliente(cli_address, cli_socket)
    cliente.start()

s.close()