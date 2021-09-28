import socket
import threading
import pandas as pd
import _pickle as cPickle

HOST = '200.239.165.217'
PORT = 8001

class cliente():
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
        self.envio_thread = threading.Thread(target=self.enviar_mensagem)
        self.receber_thread = threading.Thread(target=self.receber_mensagem)
        self.envio_thread.start()
        self.receber_thread.start()

    def enviar_mensagem(self):
        while True:
            mensagem = input("digite")
            self.s.send(mensagem.encode('utf-8'))

    def receber_mensagem(self):
        while True:
            try:
                mensagem = self.s.recv(1024).decode('utf-8')
                print(mensagem)
            except:
                print("An error occured!")
                self.s.close()
                break

cliente(HOST, PORT)
