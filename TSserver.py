
import socket as tsSoc

def TSserver():

    # Attempt to create a socket for the server
    try:
        socketServer = tsSoc.socket(tsSoc.AF_INET, tsSoc.SOCK_STREAM)
        print("[TS]: socket server created")
    except tsSoc.error as err:
        print('{} \n'.format("socket open error ", err))

    # Create Dictionary data structure
    ts_Dict = {}
    # Open file to read DNS string
    with open("PROJ1-DNSTS.txt", "r") as dnsTableFile:
        # Populate Dict data structure with hostname as key
        # And IP address and flags as values
        for fieldLine in dnsTableFile:
            dictKey = fieldLine.rstrip()
            print("[TS]: File line: ", dictKey)
            recordString = dictKey.rsplit()
            print("[TS]: line as String: ", recordString)
            hostName = recordString[0]
            ipAddress = recordString[1]
            flag = recordString[2].rstrip()
            print("[TS]: Hostname: ", hostName)
            print("[TS]: IPAddress: ", ipAddress)
            print("[TS]: Flag: ", flag)
            print()

            # Key is host name, value is a tuple of IP address and flag
            ts_Dict[hostName] = (ipAddress, flag)
            print(ts_Dict)
    
    # determine local hostname, IP address , select a port number
    host = tsSoc.gethostname()
    print("\n[TS]: got host name: ", host)
    ipAddress = tsSoc.gethostbyname(host)
    print("[TS]: IP Address: ", ipAddress)
    port = 5000
    print("[TS]: Port number: ", port, "\n")

    serverBind = ('', port)
    socketServer.bind(serverBind)
    print("[TS]: Binded IP Address and Port number: ", serverBind, "\nAlso: ", socketServer)
    print()

    print("[TS]: got host by name: %s" %tsSoc.gethostbyname(host))
    print("[TS]: got host by addr: ", tsSoc.gethostbyaddr(host))
    socketServer.listen(1)
    print("\n[TS]: Listening for one connection on port 5000...")

    clientSocket, addr = socketServer.accept()
    print("[TS]: Accepted!\n")
    
    print()

    while True:

        # Receive data that client is sending over
        givenHost = clientSocket.recv(1024).decode('utf-8')

        # If no data given, server can quit running
        if not givenHost:
            break
        print("[TS]: Client request: ", givenHost)

        # Set variable
        dataToClient = None

        # Determine if host is in the DNS table
        if givenHost in ts_Dict:
            print("[TS]: Host found")
            flag = ts_Dict[givenHost][1]
            ipAddress = ts_Dict[givenHost][0]
            dataToClient = givenHost + " " + ipAddress + " " + flag
        else:
            print("[TS]: Host not found. ERROR")
            dataToClient = givenHost + " Error: Host not found"

        clientSocket.send(dataToClient.encode('utf-8'))

    print("[TS]: clientSocket is: %s" %clientSocket)
    print("[TS]: addr is: ", addr)

    socketServer.close()

TSserver()