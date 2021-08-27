import socket
import threading
import pandas as pd
from random import sample

#HOST = '200.239.165.217'
HOST='localhost'
PORT = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

# Lista de clientes (Ip) e apelidos
clientes = []
apelidos = []
#armazenar apelido e enderço dos clientes
dic={}
#sorteio cartas
cartas=pd.read_csv('cartas.csv',sep=',')
sorteio = sample(range(0, 108), 108)

#criar relação para armazenar o clique no tira-cartas
def clique(cont):
    contador={'clique':[cont]}
    contador_csv=pd.DataFrame(contador)
    contador_csv.to_csv('contador.csv')

clique(0)
#funcao tirar carta
def tiracarta(contador):  
    global carta
    #abrir relação, somar +1, pegar o resultado e inserir como index da lista sorteio
    carta=cartas.loc[sorteio[contador]]
    print(carta)
    return carta

# Função de transmissão com restrição por código
def broadcast(mensagem,i,apelidos,dic):
    restrito=False
    for r in apelidos:
        vez='@'+r.decode('utf-8') #código
        if vez in mensagem.decode('utf-8'):
            dic[r].send(mensagem)
            i.send(mensagem) #enviando pra pessoa que escreveu também
            print(f'mensagemr restrita a {r}')
            restrito=True
    if not restrito:
        for cliente in clientes:
            print('mensagem pública')
            cliente.send(mensagem)            
            
# Função de mantimento
def handle(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            print(f"{apelidos[clientes.index(cliente)]} disse {mensagem}")
            broadcast(mensagem,cliente,apelidos,dic)
            if mensagem.decode('utf-8')=='TIRACARTA':
                contador=pd.read_csv('contador.csv')
                ordem=contador.iloc[0][1]
                ordem=ordem+1
                clique(ordem) #gravando a ordem no csv
                #colocar gravação de arquivo aqui
                cliente.send(tiracarta(ordem).encode('utf-8'))          
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            apelido = apelidos[index]
            apelidos.remove(apelido)
            break

# Função de receber novos clientes
def receive():
    while True:
        cliente, endereco = s.accept()
        print(f"Conectado com {str(endereco)}")
        cliente.send('APELIDO'.encode('utf-8'))
        apelido = cliente.recv(1024)
        apelidos.append(apelido)
        clientes.append(cliente)
        dic[apelido]=cliente
        i=cliente
        print(f"O apelido do cliente é {apelido}")
        broadcast((f'{apelido} ´ conectado ao servidor!'.encode('utf-8')),i,apelidos,dic)
        cliente.send("Conectado ao servidor".encode('utf-8'))
        t = threading.Thread(target=handle, args=(cliente,))
        t.start()        
        
print("Servidor rodando...")
receive() 

