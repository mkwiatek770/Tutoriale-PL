import socket
import pickle

HOST = '127.0.0.1'
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    obj = {"a": 1, "b": 2, "c": [12, 11, 10]}
    s.sendall(pickle.dumps(obj))
    print("Object: {} sent to server".format(obj))
