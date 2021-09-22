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
apelidos = []
dic = {}
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
    print('*ENVIADO*')


def transmitir_mensagem(mensagem, i, apelidos, dic):
    
    restrito = False
    
    for r in apelidos:
        # Codigo de restrição
        vez = '@' + r.decode('utf-8')

        if vez in mensagem.decode('utf-8'):
            dic[r].send(mensagem)
            i.send(mensagem)
            print(f'mensagemr restrita a {r}')
            restrito = True

    if not restrito:
        for cliente in clientes:
            print('mensagem pública')
            cliente.send(mensagem)            
            
            
def cabo_cliente(cliente):
    while True:
        
        try:
            mensagem = cliente.recv(1024)
            transmitir_mensagem(mensagem, cliente, apelidos, dic)
            mensagem = mensagem.decode('utf-8')
            
            if 'TIRACARTA' in mensagem:
                contador = pd.read_csv('contador.csv')
                ordem = contador.iloc[0][1]
                ordem = ordem + 1
                contagem_clique(ordem)
                tira_carta(ordem, cliente)
                print("Carta enviada com sucesso!")

            if 'pontos' in mensagem:
                for cliente in clientes:
                    print(cliente)
                    cliente.send(mensagem)

        
            
        except:
            indice = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            apelido = apelidos[indice]
            apelidos.remove(apelido)
            break


def receber_cliente():
    while True:
        cliente, endereco = s.accept()
        print(f"Conectado com {str(endereco)}")
        cliente.send('APELIDO'.encode('utf-8'))
        apelido = cliente.recv(1024)
        apelidos.append(apelido)
        clientes.append(cliente)
        dic[apelido] = cliente
        i = cliente
        print(f"O apelido do cliente é {apelido}")
        transmitir_mensagem((f'{apelido} ´ conectado ao servidor!'.encode('utf-8')), i, apelidos, dic)
        cliente.send("Conectado ao servidor".encode('utf-8'))
        t = threading.Thread(target=cabo_cliente, args=(cliente,))
        t.start()        
        
print("Servidor rodando...")
receber_cliente() 

