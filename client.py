import socket
import select
import sys

HOST = ''                 # I am using local host
PORT = 50007              # The same port as used by the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
 
while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
 
    # Using "select" here to see which is ready.
    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print message
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("You said: ")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()