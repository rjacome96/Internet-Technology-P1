
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
    rsSocketConnection = (myAddr, rsPort)

    host = aSocket.gethostname()
    print("[C]: got host name: %s" %host)
    print("[C]: got host by name: %s" %aSocket.gethostbyname(host))
    print("[C]: got host by addr: ", aSocket.gethostbyaddr(host))


    rsClientSocket.connect(rsSocketConnection)
    #tsClientSocket.connect(tsSocketConnection)

    with open("PROJ1-HNS.txt", "r") as readFile:
        with open("RESOLVED.txt", "w") as writeFile:
            for hostName in readFile:
                hostName = hostName.rstrip()
                # Stripping the new line at the end MIGHT mess with comparing strings but will need to be tested
                print()
                print("[C]: Hostname to look up: ", hostName)
                # First contact to RS server
                rsClientSocket.send(hostName.encode('utf-8'))
                #tsClientSocket.send("Search HOSTNAME".encode('utf-8'))
                print()

                flag = rsClientSocket.recv(1024).decode('utf-8')
                print("[C]: Flag received: ", flag)

                if flag == "A":
                    print()
                    ipAddress = rsClientSocket.recv(1024).decode('utf-8')
                    print("[C]: Host name: ", hostName)
                    print("[C]: IP address: ", ipAddress)
                    print("[C] Flag: ", flag)
                elif flag == "NS":
                    print()
                    serverName = rsClientSocket.recv(1024).decode('utf-8')
                    print("[C]: Gotta connect to:", serverName)
                    print("[C]: Host name: ", hostName)
                    print("[C]: Got flag: ", flag)

                #print("[C]: Message received: ", tsClientSocket.recv(1024).decode('utf-8'))


    #tsClientSocket.shutdown(aSocket.SHUT_RDWR)
    rsClientSocket.shutdown(aSocket.SHUT_RDWR)
    #tsClientSocket.close()
    rsClientSocket.close()


connectClient()