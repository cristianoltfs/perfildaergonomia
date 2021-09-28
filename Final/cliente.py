import socket
import threading
import pandas as pd
import _pickle as cPickle

HOST = 'localhost'
PORT = 8000

class cliente():
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
        self.envio_thread = threading.Thread(target=self.enviar_mensagem)
        self.envio_thread.start()

    def carta(self):
        sinal = "TIRACARTA"
        self.s.send(sinal.encode('utf-8'))
        carta_df = self.s.recv(4096)
        #decodificar a carta
        carta_recebida = cPickle.loads(carta_df)
        print(carta_recebida)
        return carta_recebida
    
    def visualizar_ranking(self):
        sinal = 'VERPONTOS'
        self.s.send(sinal.encode('utf-8'))
        ranking_df = self.s.recv(4096)
        #decodificar o df
        ranking_recebido = cPickle.loads(ranking_df)
        print(ranking_recebido)
        return(ranking_recebido)    
    
    def enviar_pontos(self,lista):
        lista_bits = cPickle.dumps(lista)
        self.s.send(lista_bits)
        print("PONTOS ENVIADOS COM SUCESSO")


#funcao abaixo pode ser apagada pela interface gráfica, no qual o botao chama a funcao diretamente
    def enviar_mensagem(self):
        while True:
            mensagem = input("digite o comando-> ")
            if 'TIRACARTA' in mensagem:
                self.carta()
            if "VERPONTOS" in mensagem:
                self.visualizar_ranking()
            if "ENVIAPONTOS" in mensagem:
                self.s.send("ENVIAPONTOS".encode('utf-8'))
                a = int(input("número do jogador de 1 a 8:"))
                b=int( input('Quantos pontos o jogador fez? '))
                lista=[0,0,0,0,0,0,0,0]
                lista[a-1]=b
                print(lista)
                self.enviar_pontos(lista)

cliente(HOST, PORT)
