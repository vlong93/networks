import socket   
import sys 
import urllib.request
import urllib.parse

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()
     
print('Socket Created')
 
host = 'www.google.com';
port = 80;
 
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
 
s.connect((remote_ip , port))
 
print('Socket Connected to ' + host + ' on ip ' + remote_ip)
 
message = "GET / HTTP/1.1\r\n\r\n".encode()
 
try :
    s.sendall(message)
except socket.error:
    print('Send failed')
    sys.exit()
 
print('Message send successfully')

reply = s.recv(4096)

print(reply)
