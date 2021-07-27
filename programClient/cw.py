import socket
import threading
import traceback

HOSTPORT = ('200.239.165.217', 12000)
#HOSTPORT = ('localhost', 12000)

# encode/decode mensanges para o servidor
def messageDecode(data):
       decoded = data.decode()
       t = int(decoded[0]) # primeiro byte e o tipo
       b = decoded[1:] # resto e o corpo
       
       return t, b
       
def messageEncode(messageType, messageBody):
    return bytes(str(messageType) + messageBody, 'utf-8')

# classe que represneta o servidor
class Server (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.socket = None
        
    def connectServer(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))
        
    def run(self):
        self.isRunning = True
        while self.isRunning:
            data = self.socket.recv(2048) # esperando por ate 2048 bytes...
            messageType, messageBody = messageDecode(data)
            
            # a decodificacao e feita por meio do 'messageType'
            if messageType == 1: # mensagem
                print(messageBody)
        
    def send(self, data):
        self.socket.sendall(data)
        
    def closeServer(self):
        self.isRunning = False

server = Server()

server.connectServer(HOSTPORT[0], HOSTPORT[1])
server.start()

username = input('Digite seu nome: ')
nroom = input('Digite o número da sala: ')

if "." in username:
    username = username.replace(".","")

usernamenroom = username + '.' + nroom

server.send(messageEncode(1, usernamenroom))

print('Entrando...')

while True:
    try:
        msg = input('Digite a mensagem: ')
        if msg == 'sair':
            server.send(messageEncode(3, msg))
        else:
            server.send(messageEncode(2, msg))
            
    except Exception as e:
        print(traceback.format_exc())
    
server.closeServer()
server.join()
