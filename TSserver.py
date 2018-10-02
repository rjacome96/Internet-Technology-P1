
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
            #print("[TS]: File line: ", dictKey)
            recordString = dictKey.rsplit()
            #print("[TS]: line as String: ", recordString)

            # From a given line in file, store host name, IP address, and flag respectively
            hostName = recordString[0]
            ipAddress = recordString[1]
            flag = recordString[2].rstrip()
            #print("[TS]: Hostname: ", hostName)
            #print("[TS]: IPAddress: ", ipAddress)
            #print("[TS]: Flag: ", flag)
            #print()

            # Key is host name, value is a tuple of IP address and flag
            ts_Dict[hostName] = (ipAddress, flag)
            #print(ts_Dict)
    
    # determine local hostname, IP address , select a port number
    port = 5000
    serverBind = ('', port)
    socketServer.bind(serverBind)
    print("[TS]: Socket is binded to port: ", port )

    socketServer.listen(1)
    print("[TS]: Listening for one connection on port 5000...")

    clientSocket, addr = socketServer.accept()
    
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

    socketServer.close()

TSserver()