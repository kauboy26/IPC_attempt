##################################

# IMPORTANT NOTE:

# I had not done inter process communication programming prior to this, and as a result
# I consulted the official Python documentation on this topic here:
# (https://docs.python.org/3/library/socket.html#socket-objects).

# I followed through the examples to understand what was happening, and tried a couple of things.
# I also consulted this guide: https://www.geeksforgeeks.org/computer-networks-set-1/g/ , and the
# other articles in that series.

##################################


import socket
import select
import sys
from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = ''                 # I am using local host
PORT = 50007   

server.bind((HOST, PORT))

server.listen(5)        # setting my limit to 5
 
list_of_clients = []
 
def clientthread(conn, addr):
    # This function will be put on to a new thread every time a connection
    # is accepted.
 
    conn.send("Send any message: ")
    # conn refers to the most recent connection (user object)
 
    while True:
            try:
                message = conn.recv(2048) # a decently sized buffer
                if message:
                    print addr[0] + ": " + message
                    message_to_send = addr[0] + ": " + message
                    broadcast(message_to_send, conn)
                else:
                    remove(conn)
 
            except:
                continue
 

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            # Basically send it to everyone who isn't the sender of this message.
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)
 
def remove(connection):
    # just remove that connection from the list of clients we have
    if connection in list_of_clients:
        list_of_clients.remove(connection)
 
while True:

    conn, addr = server.accept()

    list_of_clients.append(conn)

    print addr[0] + " connected"
 
    # creates and individual thread for every user 
    # that connects
    start_new_thread(clientthread, (conn,addr))    
 
conn.close()
server.close()