import socket
import sys
'''
Example: socket bind and listen
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
conn, addr = s.accept()

print('connected to: '+addr[0]+':'+str(addr[1]))

# receive a message
result = conn.recv(4096)
print('Client request: '+result.decode())

# send a message
conn.send(str.encode('who is there?\n'))
