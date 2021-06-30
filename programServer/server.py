import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(('',12000))

dic = {'nome':'', 'ip':'', 'port':''}

while True:
    msg, client = udp.recvfrom(2048)
#    mensagem_resposta = mensagem_bytes.decode()
#    servidor.sendto(mensagem_resposta.encode(), endereco_ip_client)
#    print(msg, client)

    if  not ((msg.decode() in dic['nome']) and (client[0] in dic['ip']) and (client[1] in dic['port'])):
        dic = {'nome':msg.decode(), 'ip':client[0], 'port':client[1]}
        print(dic)
        print('teste')
