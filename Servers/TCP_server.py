import socket
import threading
import  datetime 


IP = '100.91.176.251'
PORT = 1000

def time():
    return datetime.datetime.now()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT)) # used only on server side and not in client side
    server.listen(5)
    print(f'[{time()}] : Server Listening on {IP}:{PORT}')
    while True:
        client, ip = server.accept()
        print(f'[{time()}] : Accepted request from {ip[0]}:{ip[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
            
    



    pass
def handle_client(c_socket):
    with c_socket as sock:
        request = sock.recv(4096)
        print(f'[{time()}] : Received : {request.decode("utf-8")}')
        sock.send(b'ACK')

    pass

if __name__ == '__main__':
    main()