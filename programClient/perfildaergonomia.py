#!/usr/bin/env python3

import socket

from player import Player

HOST = '200.239.167.212'
PORT = 13333

name = 'Cristiano'
ip = '123.123.123.123'

PlayerClient = Player(name, ip)
PlayerClient.printPlayer(name, ip)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.sendall(str.encode('Bom dia Bóson!'))
data = s.recv(1024)

print('Mensagem ecoada: ', data.decode())
