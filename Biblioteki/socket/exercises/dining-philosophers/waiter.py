"""Dining philosophers problem.


            c4
 
       P5         P4

   c5                c3

P1                    P3
   
   c1            c2
      
          P2  

P = phlososopher
c = chopstick

"""

import socket
import threading


def new_client(c_socket, addr):
    while True:
        msg = c_socket.recv(1024)
        print(f"{addr} >> msg")
        c_socket.send(msg)
    c_socket.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 50000))
s.listen()  # 5 philosophers and 5 chopsticks

print("Server started!")
print("Waiting for clients")

while True:
    conn, addr = s.accept()
    threading._start_new_thread(new_client, (conn, addr))

s.close()
