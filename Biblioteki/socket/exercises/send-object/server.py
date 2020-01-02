import socket
import pickle

HOST = '127.0.0.1'
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn1, addr1 = s.accept()
    with conn1:
        obj = pickle.loads(conn1.recv(1024))
        print("Object: {} received from {}".format(obj, addr1))
        conn2, addr2 = s.accept()
        with conn2:
            conn2.send(pickle.dumps(obj))
            print("Object {} sent to {}".format(obj, addr2))
