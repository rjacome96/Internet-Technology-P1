
import socket as aSocket

def connectClient():

    try:
        rsClientSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        tsClientSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[C]: Successfully created sockets")
    except aSocket.error as err:
        print('{} \n'.format("Socket open error ", err))

    tsPort = 5000
    myAddr = aSocket.gethostbyname(aSocket.gethostname())
    tsSocketConnection = (myAddr, tsPort)

    rsPort = 6000
    rsSocketConnection2 = (myAddr, rsPort)

    host = aSocket.gethostname()
    print("[TS]: got host name: %s" %host)
    print("[TS]: got host by name: %s" %aSocket.gethostbyname(host))
    print("[TS]: got host by addr: ", aSocket.gethostbyaddr(host))

    rsClientSocket.connect(tsSocketConnection)


    rsClientSocket.send("Hey bro!".encode('utf-8'))

    rsClientSocket.shutdown(aSocket.SHUT_RDWR)
    rsClientSocket.close()


connectClient()