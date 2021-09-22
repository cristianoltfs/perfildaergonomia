import socket
import threading
import pandas as pd
import _pickle as cPickle


class cliente():
    def __init__(self, HOST, PORT, apelido):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
        self.apelido = apelido
        envio_thread = threading.Thread(target=self.enviar_mensagem)
        receber_thread = threading.Thread(target=self.receber_mensagem)
        envio_thread.start()
        receber_thread.start()
        
        
    def carta(self):
        sinal = f'{self.apelido}:{"TIRACARTA"}'
        self.s.send(sinal.encode('utf-8'))
        carta_df = self.s.recv(4096)
        #decodificar a carta
        carta_recebida = cPickle.loads(carta_df)
        return(carta_recebida)

    
    def enviar_pontos(self,lista_pontos):
        lista_pontos.append('pontos')
        lista_string = str(lista_pontos)
        self.s.send(lista_string.encode('utf-8'))

    def enviar_mensagem(self):
        while True:
            mensagem = '{}: {}'.format(self.apelido, input(''))
            self.s.send(mensagem.encode('utf-8'))    
    
    
    def receber_mensagem(self):
        while True:
            try:
                mensagem = self.s.recv(1024).decode('utf-8')
                if mensagem == 'APELIDO':
                    self.s.send(self.apelido.encode('utf-8'))

                if 'pontos' in mensagem:
                    print(f"Mensagem com pontuação: {mensagem}")
                    #from classeTabuleiro import recebePontos
                    csv = open('ptsServer.csv', 'w')
                    csv.write(mensagem)
                    csv.close()

                #recebePontos(mensagem)



                   
            except:
                print("An error occured!")
                self.s.close()
                break

