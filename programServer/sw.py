import socket
import threading
import traceback

ip = '200.239.165.217' # coloca o ip do servidor aqui
port = 17010

clients = {}

# guardar quantas pessoas tem em cada sala
sala = [0]*100

# encode/decode mensanges para o servidor
def messageDecode(data):
       decoded = data.decode()
       t = int(decoded[0]) # primeiro byte e o tipo
       b = decoded[1:] # resto e o corpo
       
       return t, b
       
def messageEncode(messageType, messageBody):
    return bytes(str(messageType) + messageBody, 'utf-8')

# essa classe vai representar o cliente dentro do servidor
class Client(threading.Thread): # esta classe herda da classe Thread
    def __init__(self, address, socket):
        threading.Thread.__init__(self)
        self.username = None
        self.address = address
        self.socket = socket
        self.nsala = None
        
    def run(self): # futuramente aqui será responsável por decodificar as mensagens de um cliente
        print('Client ' + self.address + ' se conectou')
        
        # aqui dentro a thread vai esperar por mensagens do cliente
        while True:
            try:
                data = self.socket.recv(2048) # esperando por ate 2048 bytes...
                messageType, messageBody = messageDecode(data)
                
                # a decodificacao e feita por meio do 'messageType'
                if messageType == 1: # login
                    temp = messageBody.split(".")
                    self.username = temp[0]
                    self.numsala = int(temp[1])
                    self.broadcast(1, self.username + ' entrou na sala ' + self.numsala)
                    
                    if sala[self.numsala - 1] < 4:
                        sala[self.numsala - 1] += 1
                        print(f'Você é a pessoa número: {sala[self.numsala - 1]}' )
                    else :
                        message = 'kika'
                    # PARAMOS AQUI
                    # ENVIAR MENSAGEM PRA QUEM ESTÁ NA MESMA SALA
                        self.socket.send(messageEncode(messageType, message))
                        clients.pop(self.address)
                        print('Kika', clients)
                        break


                elif messageType == 2 and sala[self.numsala] and a: # mensagem
                    self.broadcast(1, self.username + ': ' + messageBody)


                elif messageType == 3: # logout
                    clients.pop(self.address)
                    self.broadcast(1, self.username + ' saiu')
                    sala[int(self.numsala)-1] -= 1
                    break


            except Exception as e:
                print(traceback.format_exc())
                break
                
        print('Client end *** ' + self.address + ' saiu')
                    
    def sendMessage(self, messageType, message):
        try:
            self.socket.send(messageEncode(messageType, message))
        except:
            clients.pop(self.address)
        
    # envia mensagem para todos os clientes
    # ENVIAR MENSAGEM PRA QUEM ESTÁ NA MESMA SALA
    # VER A SALA DO CLIENTE E ENVIAR PRA TODOS QUE TEM A MESMA SALA
    # VARRER TODOS CLIENTES
    # CLASSE.NUSALA E VERIRICAR SE É IGUAL AO CLIENTE CORRENTE
    def broadcast(self, messageType, message):
        for address in clients:
            clients[address].sendMessage(messageType, message)
                
                
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))

print ('Server iniciado')

while True:
    server.listen(1)
    socket, addr = server.accept()
    address = str(addr)
    client = Client(address, socket)
    client.start()
    clients[address] = client
    
