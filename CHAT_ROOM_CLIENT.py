import socket

import socket 
import select 
import sys 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.connect(('127.0.0.1', 12387))
# print("ENTER THE IP YOU WANT TO CONNECT:") 
# Hostname = sys.stdin.readline()
# print("ENTER THE PORT NUMBER:")
# port = sys.stdin.readline()
print("Waiting for the connection:")
# server.settimeout(100)


# server.connect((Hostname,int(port)))
  
while True: 
  
    
    sockets_list = [sys.stdin, server] 
  
    """ There are two possible input situations. Either the 
    user wants to give  manual input to send to other people, 
    or the server is sending a message  to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else 
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
    
    for socks in read_sockets: 
        if socks == server: 
            message = socks.recv(2048).decode("utf-8") 
            if not message:
                print("Disconnected from the server")
                sys.exit()
            else:    
                print(message) 
        else: 
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<YOU>")
            sys.stdout.write(message)
            sys.stdout.flush()

            

            

server.close()            
        