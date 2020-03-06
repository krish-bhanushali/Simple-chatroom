import socket
import select
import threading as thr
import sys


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(('127.0.0.1',12387))

server.listen(20)

Client_list = []


def clientthread(connect,address):
    connect.send(bytes("welcome guys","utf-8"))
    sockets_list = [sys.stdin, connect] 
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    for socks in read_sockets:
    # while True:
        if socks == connect:
            message = connect.recv(2048).decode('utf-8')
            if not message:
                removeconnection(connect)
            else:
                print("<"+address[0]+">"+"says:"+message)
                message="<"+address[0]+">"+"says:"+message
                b_message= bytes(message,"utf-8")
                broadcast(b_message,connect) 
        else:
            #when server wants to communicate
             message = sys.stdin.readline()
             server_message = "Server said-->"+message
             sb_message = bytes(server_message,"utf-8")
             sys.stdout.write("<YOU>")
             serverbroadcast(sb_message,connect)
             sys.stdout.write(message)
             sys.stdout.flush()                  


# #to broadcast we simply send all messages to people other than sender
def broadcast(message,connection):
    for clients in Client_list:
        if clients!=connection:
            clients.send(message)

def removeconnection(connect):
    if connect in Client_list:
        left_message = "<"+address[0]+">"+" has left the chat"
        print("<"+address[0]+">"+" has left the chat")
        close_message = bytes(left_message,"utf-8")
                
        Client_list.remove(connect)
        broadcast(close_message,connect)            

def serverbroadcast(message,connection):
    for clients in Client_list:
        clients.send(message)
























while True:
    connect , address = server.accept()
    Client_list.append(connect)
    print("<"+address[0]+">"+" "+"JOINS THE ARENA")
    
 #starting a new thread for each user, that is now we dont need to handle users one by one we can handle them using threads parellely
    thr._start_new_thread(clientthread,(connect,address))


connect.close()
server.close()    




