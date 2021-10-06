import socket
import threading
import _pickle as cPickle
import time
HOST = '200.239.165.217'

PORT = 8000
#HOST = 'localhost'
class cliente():
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
        #self.envio_thread = threading.Thread(target=self.enviar_mensagem)
       # self.envio_thread.start()
        #self.enviar_mensagem()

    def carta(self):
        sinal = "TIRACARTA"
        self.s.send(sinal.encode('utf-8'))
        carta_df = self.s.recv(4096)
        #decodificar a carta
        carta_recebida = cPickle.loads(carta_df)
        print(carta_recebida)
        print('Carta recebida com sucesso!')
        return carta_recebida
    
    def visualizar_ranking(self):
        sinal = 'VERPONTOS'
        self.s.send(sinal.encode('utf-8'))
        ranking_df = self.s.recv(4096)
        #decodificar o df
        ranking_recebido = cPickle.loads(ranking_df)
        print(ranking_recebido)
        return(ranking_recebido)    
    
    def enviar_pontos(self, lista):
        self.s.send("ENVIAPONTOS".encode('utf-8'))
     #   a = int(input("número do jogador de 1 a 8:"))
      #  b = int(input('Quantos pontos o jogador fez? '))
       # lista = [0, 0, 0, 0, 0, 0, 0, 0]
        print(lista)

        lista_bits = cPickle.dumps(lista)
        self.s.send(lista_bits)
        print("PONTOS ENVIADOS COM SUCESSO")
        
        
    def envia_meu_nome(self,a):
        sinal = 'MEUNOME'
        self.s.send(sinal.encode('utf-8'))
        nome_bits = a.encode('utf-8')      
        time.sleep(0.5)
        self.s.send(nome_bits)
        print("NOME ENVIADO COM SUCESSO")



"""#funcao abaixo pode ser apagada pela interface gráfica, no qual o botao chama a funcao diretamente
    def enviar_mensagem(self, mensagem):
        while True:
            try:
              #  mensagem = input("digite o comando-> ")
               # if 'TIRACARTA' in mensagem:
               #     self.carta()
                if "VERPONTOS" in mensagem:
                    self.visualizar_ranking()
                if "ENVIAPONTOS" in mensagem:
                    self.s.send("ENVIAPONTOS".encode('utf-8'))
                    a = int(input("número do jogador de 1 a 8:"))
                    b = int( input('Quantos pontos o jogador fez? '))
                    lista = [0, 0, 0, 0, 0, 0, 0, 0]
                    lista[a - 1] = b
                    print(lista)
                    self.enviar_pontos(lista)
                if "MEUNOME" in mensagem:
                    apelido = input("Digite seu nome: ")
                    self.envia_meu_nome(apelido)
            except:
                pass"""



