
import socket as aSocket

def connectClient():

    try:
        rsClientSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        tsClientSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[C]: Successfully created sockets")
    except aSocket.error as err:
        print('{} \n'.format("Socket open error ", err))

    """
    host = aSocket.gethostname()
    print("[C]: got host name: %s" %host)
    print("[C]: got host by name: %s" %aSocket.gethostbyname(host))
    print("[C]: got host by addr: ", aSocket.gethostbyaddr(host))
    """

    rsPort = 6000
    rsHostName = input("[C]: Enter address of RS server: ")
    rsAddr = aSocket.gethostbyname(rsHostName)
    rsSocketConnection = (rsAddr, rsPort)

    rsClientSocket.connect(rsSocketConnection)
    serverConnected = False

    with open("PROJ1-HNS.txt", "r") as readFile:
        with open("RESOLVED.txt", "w") as writeFile:
            for hostName in readFile:
                # Stripping the new line at the end MIGHT mess with comparing strings but will need to be tested
                hostName = hostName.rstrip()
                #print()
                #print("[C]: Hostname to look up: ", hostName)
                # First contact to RS server
                rsClientSocket.send(hostName.encode('utf-8'))
                #print()

                # Get resulting String from server
                serverResult = rsClientSocket.recv(1024).decode('utf-8')

                # Split the strings into 3 parts (HostName, IPaddress, Flag)
                result = serverResult.split()

                # Select the flag
                flag = result[2].rstrip()
                #print ("[C]: Flag is: ", flag)
                
                # Set variable to write to file

                if flag == "A":
                    print()
                    print("[C]: Result from RS server ", serverResult)
                elif flag == "NS":
                    print()
                    serverName = result[0]
                    #print("[C]: Gotta connect to:", serverName)
                    #print("[C]: Host name: ", hostName)
                    #print("[C]: Got flag: ", flag)

                    if not serverConnected:
                        tsPort = 5000
                        #tsAddr = aSocket.gethostbyname(serverName)
                        # THE COMMENTED OUT LINE ABOVE SHOULD BE UNCOMMENTED IN THE END AND THE BOTTOM LINE DELETED
                        tsAddr = aSocket.gethostbyname(aSocket.gethostname())
                        tsSocketConnection = (tsAddr, tsPort)
                        tsClientSocket.connect(tsSocketConnection)
                        #print("[C]: Connected to TS server")
                        serverConnected = True
                         
                    tsClientSocket.send(hostName.encode('utf-8'))
                    serverResult = tsClientSocket.recv(1024).decode('utf-8')
                    print("[C]: Result from TS server: ", serverResult)

                writeFile.write(serverResult + "\n")


    tsClientSocket.shutdown(aSocket.SHUT_RDWR)
    rsClientSocket.shutdown(aSocket.SHUT_RDWR)
    tsClientSocket.close()
    rsClientSocket.close()


connectClient()