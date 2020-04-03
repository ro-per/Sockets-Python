import socket

'''
This example demonstrates a simple port scanner
using Python
'''

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'tweakers.net' 

def pscan(port):  
    try:
        s.connect((server,port))
        return True
    except:
        return False    

ports = [21,80,443]

    
for p in ports:
    if pscan(p):
        print('Port ',p,' is open!')
    else:
        print('Port ',p,' is closed!')
