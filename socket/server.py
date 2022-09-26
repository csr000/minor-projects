import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1235))
server.listen()

while True:
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))