
import socket as aSocket

def RSserver():

    try:
        socketServer = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[RS]: Successfully created socket")
    except aSocket.error as err:
        print('{}\n'.format("Socket open error ", err))

    with open("PROJ1-DNSRS.txt", "r") as dnsTableFile:
        for fieldLine in dnsTableFile:
            print("[RS]: File line: ", fieldLine)


    port = 6000
    serverBinding = ('', port)
    socketServer.bind(serverBinding)
    print("[RS]: Socket is binded to port: ", port )
    
    socketServer.listen(1)
    print("[RS]: Listening for one connection on port 6000...")
    clientSocket, addr = socketServer.accept()

    while True:

        print("[RS]: Request found: ", clientSocket.recv(1024).decode('utf-8'))
        clientSocket.send("RS Server here".encode('utf-8'))
        dataFromClient = clientSocket.recv(1024).decode('utf-8')
        if not dataFromClient:
            break
    

    socketServer.close()
RSserver()