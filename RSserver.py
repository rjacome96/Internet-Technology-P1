
import socket as aSocket

def RSserver():

    # Attempt to create a socket for server
    try:
        socketServer = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[RS]: Successfully created socket")
    except aSocket.error as err:
        print('{}\n'.format("Socket open error ", err))

    # We will find the server's host name when we come across 'NS' in the file
    serverToConnect = None
    # Create Dictionary data structure as DNS table
    rs_Dict = {}
    # Read lines from file
    with open("PROJ1-DNSRS.txt", "r") as dnsTableFile:
        # Populate Dict data structure with hostname as key
        # And IP address and flags as values
        for fieldLine in dnsTableFile:
            dictKey = fieldLine.rstrip()
            #print("[RS]: File line: ", dictKey)
            recordString = dictKey.rsplit()
            #print("[RS]: line as String: ", recordString)

            # From a given line in file, store host name, IP address, and flag respectively
            hostName = recordString[0]
            ipAddress = recordString[1]
            flag = recordString[2].rstrip()

            if flag == "NS":
                # Found the server that will redirect us later to TS server
                serverToConnect = hostName
            #print("[RS]: Hostname: ", hostName)
            #print("[RS]: IPAddress: ", ipAddress)
            #print("[RS]: Flag: ", flag)
            #print()

            # Key is host name, value is a tuple of IP address and flag
            rs_Dict[hostName] = (ipAddress, flag)
            #print(rs_Dict)

    # Pick port and bind it to this machine's IP address
    port = 6000
    serverBinding = ('', port)
    socketServer.bind(serverBinding)
    print("[RS]: Socket is binded to port: ", port )
    
    # Have socket listen on the port
    socketServer.listen(1)
    print("[RS]: Listening for one connection on port 6000...")
    clientSocket, addr = socketServer.accept()

    # Once connected, service the client until the end
    while True:
        
        # Get host name client is looking for
        givenHost = clientSocket.recv(1024).decode('utf-8')
        print("[RS]: Client request: ", givenHost)

        # Client essentially closed its socket (or literally sent nothing)
        if not givenHost:
            break

        # set variable
        dataToClient = None

        # Host name is in RS server's DNS table
        if givenHost in rs_Dict:
            print("[RS]: Host found")
            flag = rs_Dict[givenHost][1]
            dataToClient = givenHost + " " + rs_Dict[givenHost][0] + " " + flag
        else:
            print("[RS]: Host not found. Redirect to TS")
            flag = "NS"
            dataToClient = serverToConnect + " - " + flag
        
        print("[RS]: Sending hostname to client: ", dataToClient)
        clientSocket.send(dataToClient.encode('utf-8'))
    

    socketServer.close()
RSserver()