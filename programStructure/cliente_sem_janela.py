import socket
import threading
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
    
        
    def visualizar_ranking(self):
        sinal = '98989898355531'
        self.s.send(sinal.encode('utf-8'))
        ranking_df = self.s.recv(4096)
        #decodificar o df
        ranking_recebido = cPickle.loads(ranking_df)
        return(ranking_recebido)    

    
    def enviar_pontos(self,lista_pontos):
        sinal = '989898983'
        lista_pontos.append(sinal)
        lista_string = str(lista_pontos)
        self.s.send(lista_string.encode('utf-8'))
        print(lista_pontos)

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
                else:
                    print("11111111111111111")
                    print(mensagem)
                    print("22222222222222222")
                   
            except:
                print("An error occured!")
                self.s.close()
                break