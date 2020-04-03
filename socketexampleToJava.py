import socket

'''
This example demonstrates a simple socket connection
'''

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)


# server name and port
server = '10.129.182.27' # localhost
port = 9999

# get ip adress by server name
server_ip = socket.gethostbyname(server)
print(server_ip)

request = "Knock, knock!\n"

# connect and send request
s.connect((server,port))
s.send(request.encode()) # the string must be decoded to a byte string

# get result, where 4096 is the max buffer size
result = s.recv(4096)

print("Server's answer: "+result.decode())
