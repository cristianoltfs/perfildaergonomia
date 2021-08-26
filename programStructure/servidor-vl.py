import socket
import threading

# Detalhes do servidor
#HOST = '200.239.165.217'
HOST = 'localhost'
PORT = 8000

# Iniciar o servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

# Lista de clientes (Ip) e apelidos
clientes = []
apelidos = []
marcado = 0
dic = {}
# Função de transmissão
def broadcast(mensagem,i,apelidos,dic):

    #exclusao=clientes.copy()
    restrito=False
    for r in apelidos:
        vez = '@' + r.decode('utf-8')
        if vez in mensagem.decode('utf-8'):
            dic[r].send(mensagem)
            i.send(mensagem) #enviando pra pessoa que escreveu também
            print(f'mensagemr restrita a {r}')
            #exclusao.remove(dic[r])
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
            i = cliente
            print(f"{apelidos[clientes.index(cliente)]} disse {mensagem}")
            broadcast(mensagem, i, apelidos, dic)
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


        #cliente.send('SENHA'.encode('utf-8'))
        #senha = cliente.recv(1024)
        
        #if verificaLogin(apelido, senha):
        apelidos.append(apelido)
        clientes.append(cliente)
        dic[apelido] = cliente
        i = cliente

        print(f"O apelido do cliente é {apelido}")
        #print(f"A senha do cliente é {senha}")
        broadcast((f'{apelido} está conectado ao servidor!'.encode('utf-8')), i, apelidos, dic)
        cliente.send("Conectado ao servidor".encode('utf-8'))
        t = threading.Thread(target=handle, args=(cliente,))
        t.start()
        #else:
            #cliente.send('WRONG'.encode('utf-8'))
            #cliente.close()"""
        

"""def verificaLogin(apelido, senha):
    verf = False
    with open('Users.txt', 'r') as userst:
        users = userst.readlines()
        users = list(map(lambda x: x.replace('\n', ''), users))
        #print(users)
        for i in range(0, len(users) - 1, 2):
            print(f'Usuário {i}: {users[i]}\nSenha {i}: {users[i + 1]}')
            if str(apelido) == users[i] and str(senha) == users[i + 1]:
                verf = True
        return verf"""

print("Servidor rodando...")
receive() 

