
import socket as aSocket

def RSserver():

    rs_Dict = {}

    rs_Dict["HostName"] = ("123.4.2", "A")
    
    print(rs_Dict)
    print(rs_Dict["HostName"])
    print(rs_Dict["HostName"][0])
    print(rs_Dict["HostName"][1])
    rs_Dict.clear()

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
            flag = recordString[2].rstrip()
            print("[RS]: Hostname: ", hostName)
            print("[RS]: IPAddress: ", ipAddress)
            print("[RS]: Flag: ", flag)
            print()

            rs_Dict[hostName] = (ipAddress, flag)
            print(rs_Dict)
            

    print("Key is: e.yahoo.com, Value is: ", rs_Dict["e.yahoo.com"])
    print("Get the specific values: ", rs_Dict["e.yahoo.com"][0])
    print(rs_Dict["e.yahoo.com"][1])

    port = 6000
    serverBinding = ('', port)
    socketServer.bind(serverBinding)
    print("[RS]: Socket is binded to port: ", port )
    
    socketServer.listen(1)
    print("[RS]: Listening for one connection on port 6000...")
    clientSocket, addr = socketServer.accept()

    while True:
        
        givenHost = clientSocket.recv(1024).decode('utf-8')
        print("[RS]: Client request: ", givenHost)
        if not givenHost:
            break

        if givenHost in rs_Dict:
            dataToClient = rs_Dict[givenHost][1]
            clientSocket.send(dataToClient.encode('utf-8'))
            dataToClient = rs_Dict[givenHost][0]
        else:
            #Redirect to TS Server
            dataToClient = "NS"
            clientSocket.send(dataToClient.encode('utf-8'))
            dataToClient = "ilab2.cs.rutgers.edu"
        
        clientSocket.send(dataToClient.encode('utf-8'))
    

    socketServer.close()
RSserver()