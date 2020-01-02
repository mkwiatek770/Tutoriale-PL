import socket

HOST = '127.0.0.1'
PORT = 65429

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    # conn, addr = s.accept()

    conn1, addr1 = s.accept()

    with conn1:
        print("Connected by ", addr1)
        conn2, addr2 = s.accept()
        with conn2:
            print("Connected by ", addr2)
            letter = conn1.recv(1024)
            conn1.sendall(letter)

            decremented_letter = chr(ord(letter) - 1)
            conn2.sendall(bytes(decremented_letter.encode("utf-8")))
