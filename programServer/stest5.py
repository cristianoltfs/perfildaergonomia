import socket
import threading

HOST = '200.239.165.217'
PORT = 13333

class Cliente(threading.Thread):
    def __init__(self, cli_address, cli_socket):
        threading.Thread.__init__(self)
        self.username = cli_socket.recv(1024)
        self.csocket = cli_socket
        self.caddress = cli_address
        print ("Nova conexão player: ", self.username.decode(), cli_address)
    def run(self):
        self.csocket.sendall(str.encode('teste'))




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
print("Servidor inicializado!")
print("Esperando conxão de clientes!")

while True:
    s.listen()
    cli_socket, cli_address = s.accept()
#    print('Conecado ao IP', cliAddress[0], 'e porta', cliAddress[1])
#    cliSocket.send(str.encode('mensagem ç teste enviada pelo server','UTF-8'))
    cliente = Cliente(cli_address, cli_socket)
    cliente.start()

s.close()