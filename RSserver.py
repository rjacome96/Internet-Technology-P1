
import socket as aSocket

def RSserver():

    try:
        socketServer = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[RS]: Successfully created socket")
    except aSocket.error as err:
        print('{}\n'.format("Socket open error ", err))

    port = 6000
    serverBinding = ('', port)
    socketServer.bind(serverBinding)
    print("Socket is binded to port: ", port )

    socketServer.listen(1)
    clientSocket = socketServer.accept()

    clientSocket.send("RS Server here".encode('utf-8'))
    

    socketServer.close()
RSserver()