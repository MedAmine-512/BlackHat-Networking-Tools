import socket 

target_host = "www.google.com"
target_port = 80



# AF_INET parameter indicates we’ll use a standard IPv4, SOCK_STREAM indicates that this will be a TCP client
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

client.connect((target_host,target_port))


# Data sent in Bytes to the target host
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

'''
The b before the string (b"...") means that this is a byte string in Python.
When working with sockets, data is usually sent and received in bytes rather than regular strings.

'''



responde = client.recv(4096) # 4Kb

'''
4096  represents the buffer size, meaning the maximum number of bytes the program will read from the server's response at a time.

It can be changed response by using a loop till no more data is received


while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    response += chunk

print(response.decode())  # Print full response



'''

print(responde.decode())


client.close()

