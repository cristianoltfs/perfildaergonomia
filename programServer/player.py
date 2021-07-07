class Player():

    '''Essa classe vai ser de utilizada para cada jogador'''

    def __init__(self, id, name, ip):
        self.id = id
        self.name = name
        self.ip = ip
        
    
    def printPlayer(self, name, ip):
        print('Player : %s %s' %(name, ip))


numJogadores = 32
listaJogadores = [0] * numJogadores
id = 1
nome = 'ç'
ip = '2'

listaJogadores.insert(listaJogadores.index(0), id)
for i in range(3):
    a = "jogador" + str(listaJogadores[i])
    jogador1 = Player(id, nome, ip)
    globals()[f"jogador{listaJogadores[i]}"] = Player(id, nome, ip)
    
    #print(a.name)
    print(jogador1.ip)
    print(jogador1.id)
    print(jogador1.name)