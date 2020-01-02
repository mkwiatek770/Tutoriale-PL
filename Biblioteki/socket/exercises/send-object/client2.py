import socket
import pickle

HOST = '127.0.0.1'
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    obj = pickle.loads(s.recv(1024))
    print("Object: {} received from server".format(obj))
    print(obj['a'])
