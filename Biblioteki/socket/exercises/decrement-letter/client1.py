import socket

HOST = '127.0.0.1'
PORT = 65429
LETTER = "z"

# connect to server and send letter
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(LETTER.encode("utf-8"))
    print(f"Letter {LETTER} sent to server to decrement")
