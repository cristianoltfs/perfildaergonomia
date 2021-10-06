import socket
import threading
import pandas as pd
from random import sample
import _pickle as cPickle
HOST = 'localhost'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
clientes = []

cartas = pd.read_csv('cartas.csv', sep=';')
sorteio = sample(range(0, 108), 108)


def contagem_clique(cont):
    contador = {'clique': [cont]}
    contador_csv = pd.DataFrame(contador)
    contador_csv.to_csv('contador.csv')    
contagem_clique(0)


def tira_carta(contador,cliente):
    carta = cartas.loc[sorteio[contador]]
    carta_bits = cPickle.dumps(carta)
    print(carta)
    cliente.send(carta_bits)
    

def armazenamento_pontos(pontuacao):
    pontos =  {'pontos':pontuacao}
    pontos_csv =  pd.DataFrame(pontos)
    pontos_csv.to_csv('pontuação.csv')
    
armazenamento_pontos([0,0,0,0,0,0,0,0]) #iniciando arquivo

def envio_pontos(cliente):
    pontos_csv = pd.read_csv('pontuação.csv') #lendo arquivo
    pontos_bits = cPickle.dumps(pontos_csv)
    print(pontos_csv)
    cliente.send(pontos_bits)

    print('* PONTOS ENVIADOS *')

#OBSOLETO
def transmitir_mensagem(mensagem):
    for cliente in clientes:
        print('mensagem pública enviada')
        cliente.send(mensagem)
        print(mensagem)    
        
        
def cabo_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            #transmitir_mensagem(mensagem)
            mensagem = mensagem.decode('utf-8')
          
            if 'TIRACARTA' in mensagem:
                contador = pd.read_csv('contador.csv')
                ordem = contador.iloc[0][1]
                ordem = ordem + 1
                contagem_clique(ordem)
                tira_carta(ordem, cliente)
                print("Carta enviada com sucesso!")        
                
            if 'ENVIAPONTOS' in mensagem:
                esperando_lista = cliente.recv(1024)
                valores =list( cPickle.loads(esperando_lista))
                print(valores)
                
                somar_pontos = pd.read_csv('pontuação.csv') #lendo arquivo
                somar_pontos = list(somar_pontos['pontos'])
                soma = list(map(lambda v1, v2: v1 + v2, somar_pontos,valores))
                armazenamento_pontos(soma) #chamando funcao/salvando somatorio de pontos
                print("PONTOS GRAVADOS NO SERVIDOR COM SUCESSO, SOLICITE PARA VISUALIZAR")

            if 'VERPONTOS' in mensagem:
                envio_pontos(cliente)
                
                
            if "MEUNOME" in mensagem:
                esperando_nome = cliente.recv(1024)
                nome = esperando_nome.decode('utf-8')
                mensagem = '{}, {}'.format(nome, 'Seu nome está aqui no servidor!')
                print(mensagem)
                
        except:
            clientes.remove(cliente)
            cliente.close()
            break

def receber_cliente():
    while True:
        cliente, endereco = s.accept()
        clientes.append(cliente)
        print((str(endereco) + " SE CONECTOU NO SERVIDOR"))
        t = threading.Thread(target=cabo_cliente, args=(cliente,))
        t.start()        
        
print("Servidor rodando...")
receber_cliente() 

