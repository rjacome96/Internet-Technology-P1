# Internet-Technology-P1
Create a DNS between two servers and a client.

Project 1

October 15, 2018

Professor Badri Nath

Roy Jacome & Kishan Patel

How to connect the client to servers: Client assumes that RS server is on the same machine/host that the Client is running on. The TS server on the other hand should run on the host grep.cs.rutgers.edu

NOTE: The TS host machine we use to run our code on is grep.cs.rutgers.edu

NOTE: The environment used to build the python code is Python 3.6. Whenever ran, we would use the python command: python3 <file.py>. Using this command we are able to run the programs of each file.

Client connects to RS server to look up host name. If found, return, host name, IP address and flag as a string. Else, RS server tells client to redirect to TS server by giving TS's host name. Client connects to TS server. If host name found, return the host name, ipaddress,flag as a string. Else, return error message.

As of this point, the code has been tested against different machines (personal and ilab) and the programs run to completion as well as outputting the correct solution from the given test files.

Both servers (RS and TS) loop through their respective files (DNS tables) and store them in their respective Dictionaries. Where the host name is the key and (IPaddress, flag) are the values.

Client will first connect to RS server to ask for the host names. When RS server does not find the host name in its data structure, it uses the other server's host name to send back to the client. Once client receives the "NS" flag, it will check if this is the first time it connects to the TS server with a boolean value. If it already did, do not connect again, else connect to the server and stay connected.

Servers will run as long as the client needs them for. When the client disconnects, the servers disconnect as well becasue they assume client is finished. This is designed so that servers will close their sockets properly even when client crashes. (This helps us to quickly test our code again without needing to wait for the ports/sockets to finish closing)

NOTE: As mentioned above, the client will not connect to the TS server until the RS server redirects the client to do so. Once the client connects to the TS server, it will stay connected until the entirety of the client's program. Thus, client does its best to simulate going from one server to the other but once connected to a server, it stays connected until the end.

NOTE: All files/programs assume that there will ONLY be two servers that the client will connect to. Client only creates two sockets. We also assume that the RS server will only be given ONE "NS" flagged entry (which is presumably the TS server's host name) as it saves its name in the beginning while storing the fields into its data structure. Client also assumes RS server is running on the same machine as the client so it connects to the local host.