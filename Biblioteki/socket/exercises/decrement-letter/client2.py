import socket

HOST = '127.0.0.1'
PORT = 65429

# connect to server and listen for letter from server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        letter = s.recv(1024)
        s.sendall(letter)
        if letter:
            print("Decremented letter: ", letter.decode("utf-8"))
            break
