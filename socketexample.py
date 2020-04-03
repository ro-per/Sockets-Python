import socket

'''
This example demonstrates the usage of a basic HTTP request with a socket in python
'''

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

#
#
#
#
#

#
#
#
#

#
#
#
#

#
#
#
#

#
#
#
#

#
#
#
#

#
#
#
#

# server name and port
server = 'wikipedia.org'
port = 80

# get ip adress by server name
server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

# connect and send http request
s.connect((server,port))
s.send(request.encode()) # the string must be decoded to a byte string

# get result, where 4096 is the max buffer size
result = s.recv(4096)

#print(result)

# print buffered results one by one
while(len(result) > 0):
    print(result)
    result = s.recv(1024)
