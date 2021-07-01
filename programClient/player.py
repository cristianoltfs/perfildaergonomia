class Player():

    '''Essa classe vai ser de utilizada para cada jogador'''

    def __init__(self, name, ip):
    
        self.name = name
        self.ip = ip
    
    def printPlayer(self, name, ip):
        print('Player : %s %s' %(name, ip))
