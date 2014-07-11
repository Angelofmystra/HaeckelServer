#!/usr/bin/env python
import select
import socket
import sys
from commands import parse                                             # the commands.py that I have made


host = ''                                                               # '' means its the local host name
port = 50000                                                            # a 5 digit port number was used since that is a standard for MUD clients
backlog = 5                                                             # No idea what this does
size = 1024                                                             # Limits the size of a packet the server will RECEIVE, not SEND. This has neglible effect for the server end.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              # Starts up the socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)            # Makes it such that the socket connection with clients is a persistent connection
server.bind((host,port))
server.listen(backlog)
input = [server,sys.stdin]                                              # This uses what is known as the select.select method. It is asynchronous multiplexing. It is allegedly the best way.
running = 1
print "Listening for incoming connections..."
while running:
    inputready,outputready,exceptready = select.select(input,[],[])     # The server uses the .select() call to multiplex multiple clients
    for s in inputready:

        if s == server:
                                                                        # handle the server socket
            client, address = server.accept()
            input.append(client)
            print "[+] New thread started for %s"% str(address) 
        elif s == sys.stdin:
                                                                        # handle standard input
            junk = sys.stdin.readline()
            print "Server disconnected..."
            running = 0

        else:
                                                                        # handle all other sockets
            data = s.recv(size)
            if data:
                print "data rcv: "+data
                data = parse(data)
                print "data snd: "+data
                s.send(data)                                            # The parse command is run from the commands.py file
            else:
                print "%s disconnected improperly."% s                  # Indicates if a client disconnected properly
                s.close()
                input.remove(s)
server.close()


