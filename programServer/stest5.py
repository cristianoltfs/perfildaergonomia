import socket
import threading

HOST = '200.239.165.217'
PORT = 13333

clients = {}

# iniciando uma lista com 0 pessoas
# em cada uma das 100 salas
# salas = ["n"] * 100

class Sala():
    def __init__(self, sala):
        self.nsala = sala

class Cliente(threading.Thread):
    def __init__(self, cli_address, cli_socket):
        threading.Thread.__init__(self)
        self.username = cli_socket.recv(1024)
        self.csocket = cli_socket
        self.caddress = cli_address
        self.sala = 0
        print ("Nova conexão. Player: ", self.username.decode(), cli_address, "Conectado")
    def run(self):
        self.sala = self.csocket.recv(1024)
#            try: # verificar se a sala existe
#                self.sala # verificar se a sala existe
#            except: # se não existir, criar
#                self.sala = Sala(self.sala)
#            self.sala7 = Sala(self.sala, self.username)
#            print(globals()[f"sala{self.sala}"])
#            globals()[f"sala{self.sala}"] = Sala(self.sala, self.username)
#            self.globals()[f"sala{sala}"] = Sala(self.sala, self.username)
        self.csocket.sendall(self.username + bytes(' você está conectado na sala ','UTF-8') + self.sala)
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'sair' or msg == '':
                break
            print ("Mensagem do cliente: ", msg)
            #self.csocket.sendall(bytes(msg,'UTF-8'))
            
#            for cli_address in clients:
#                clients[cli_address].csocket.sendall(msg.encode())
                
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
    clients[cli_address] = cliente

s.close()
