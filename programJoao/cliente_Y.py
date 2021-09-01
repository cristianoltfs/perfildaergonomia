import socket
import threading

    
def cliente(HOST,PORT,nick):
    apelido = nick

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
    cliente.connect((HOST, PORT))
    
    
    def receber_mensagem():
        while True:
            try:
                mensagem = cliente.recv(1024).decode('utf-8')
                if mensagem == 'APELIDO':
                    cliente.send(apelido.encode('utf-8'))
                else:
                    print(mensagem)
                    
            except:
                print("An error occured!")
                cliente.close()
                break
            
            
    def enviar_mensagem():
        while True:
            mensagem = '{}: {}'.format(apelido, input(''))
            cliente.send(mensagem.encode('utf-8'))
    
    
    receive_thread = threading.Thread(target=receber_mensagem)
    receive_thread.start()
    
    write_thread = threading.Thread(target=enviar_mensagem)
    write_thread.start()
