
import socket as tsSoc

def TSserver():

    try:
        socketServer = tsSoc.socket(tsSoc.AF_INET, tsSoc.SOCK_STREAM)
        print("[TS]: socket server created")
    except tsSoc.error as err:
        print('{} \n'.format("socket open error ", err))
    
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
    print("\n[TS]: Listening for one connection...")

    ctsd, addr = socketServer.accept()
    print("[TS]: Accepted!\n")
    
    print()

    print("What if we are waiting to receive anything but client doesn't do anything?")

    # Receive data that client is sending over
    clientReq = ctsd.recv(1024).decode('utf-8')

    """
    if clientReq in ts_table:
        entry = TS_table(clientReq)
    else:
        entry = "hname" + "Error: Host not found"
    
    ctsd.send(entry)
    """
    print("[TS]: ctsd is: %s" %ctsd)
    print("[TS]: addr is: ", addr)

    socketServer.close()

TSserver()