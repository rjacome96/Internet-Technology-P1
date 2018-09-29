
import socket as aSocket

def RSserver():

    # Attempt to create a socket for server
    try:
        socketServer = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[RS]: Successfully created socket")
    except aSocket.error as err:
        print('{}\n'.format("Socket open error ", err))

    # Create Dictionary data structure as DNS table
    rs_Dict = {}
    # Read lines from file
    with open("PROJ1-DNSRS.txt", "r") as dnsTableFile:
        # Populate Dict data structure with hostname as key
        # And IP address and flags as values
        for fieldLine in dnsTableFile:
            dictKey = fieldLine.rstrip()
            print("[RS]: File line: ", dictKey)
            recordString = dictKey.rsplit()
            print("[RS]: line as String: ", recordString)
            hostName = recordString[0]
            ipAddress = recordString[1]
            flag = recordString[2].rstrip()
            print("[RS]: Hostname: ", hostName)
            print("[RS]: IPAddress: ", ipAddress)
            print("[RS]: Flag: ", flag)
            print()

            # Key is host name, value is a tuple of IP address and flag
            rs_Dict[hostName] = (ipAddress, flag)
            print(rs_Dict)
            

    print("Key is: e.yahoo.com, Value is: ", rs_Dict["e.yahoo.com"])
    print("Get the specific values: ", rs_Dict["e.yahoo.com"][0])
    print(rs_Dict["e.yahoo.com"][1])

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
            dataToClient = rs_Dict[givenHost][1]
            clientSocket.send(dataToClient.encode('utf-8'))
            dataToClient = rs_Dict[givenHost][0]
        else:
            print("[RS]: Host not found. Redirect to TS")
            #Redirect to TS Server
            # Hardcoding this is probably the wrong way to go about this
            #But I have no idea how to search the Dict by value to get the NS value which would give us the 
            #ilab hostname key
            dataToClient = "NS"
            clientSocket.send(dataToClient.encode('utf-8'))
            dataToClient = "ilab2.cs.rutgers.edu"
        
        clientSocket.send(dataToClient.encode('utf-8'))
    

    socketServer.close()
RSserver()