import socket
import sys
from _thread import *

'''
Example: more advanced socket bind and listen
'''

host=''
port=9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

# listen on incoming connections
# 5 is the queue size (number of incoming connections)
s.listen(5)


def threaded_client(conn):
    # send a message
    conn.send(str.encode('who is there?\n'))

    while True:
        data = conn.recv(2048)
        print('received: '+data.decode())
        reply = 'server echo: '+data.decode()+'\n'
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))

    start_new_thread(threaded_client,(conn,))
