
import socket as aSocket

def RSserver():

    dictionary = {}

    dictionary["HostName"] = ("123.4.2", "A")
    
    print(dictionary)
    print(dictionary["HostName"])
    print(dictionary["HostName"][0])
    print(dictionary["HostName"][1])
    dictionary.clear()

    try:
        socketServer = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[RS]: Successfully created socket")
    except aSocket.error as err:
        print('{}\n'.format("Socket open error ", err))

    with open("PROJ1-DNSRS.txt", "r") as dnsTableFile:
        for fieldLine in dnsTableFile:
            dictKey = fieldLine.rstrip()
            print("[RS]: File line: ", dictKey)
            recordString = dictKey.rsplit()
            print("[RS]: line as String: ", recordString)
            hostName = recordString[0]
            ipAddress = recordString[1]
            flag = recordString[2]
            print("[RS]: Hostname: ", hostName)
            print("[RS]: IPAddress: ", ipAddress)
            print("[RS]: Flag: ", flag)
            print()

            dictionary[hostName] = (ipAddress, flag)
            print(dictionary)
            

    print("Key is: e.yahoo.com, Value is: ", dictionary["e.yahoo.com"])
    print("Get the specific values: ", dictionary["e.yahoo.com"][0])
    print(dictionary["e.yahoo.com"][1])
    exit()

    port = 6000
    serverBinding = ('', port)
    socketServer.bind(serverBinding)
    print("[RS]: Socket is binded to port: ", port )
    
    socketServer.listen(1)
    print("[RS]: Listening for one connection on port 6000...")
    clientSocket, addr = socketServer.accept()

    while True:

        clientSocket.send("RS Server here".encode('utf-8'))
        dataFromClient = clientSocket.recv(1024).decode('utf-8')
        print("[RS]: Request found: ", dataFromClient)
        if not dataFromClient:
            break
        """
        if clientReq in ts_table:
            entry = TS_table(clientReq)
        else:
            entry = "hname" + "Error: Host not found"
        
        ctsd.send(entry)
        break
        """
    

    socketServer.close()
RSserver()