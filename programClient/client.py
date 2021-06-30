import socket

HOSTPORT = ('200.239.167.212', 12000)

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nome = 'Cristiano'
cliente.sendto(nome.encode(), HOSTPORT)

while True:
    
    msg = input('Digite a mensagem: ')
    cliente.sendto(msg.encode(), HOSTPORT)
