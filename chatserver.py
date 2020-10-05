import socket
from threading import Thread

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server="127.0.0.1"

port=4455
s.bind((server,port))
print("Server is Running On "+ server+ ".")

s.listen(1)
conn,addr=s.accept()
print("connected")
print(addr)

class send(Thread):
    def run(self):
        while True:
            msg=input("Enter your message: ")
            print("")
            msg=msg.encode()
            conn.send(msg)
            print("Your message is sent!")

class recieve(Thread):
    def run(self):
        while True:
            r_msg=conn.recv(1024)
            r_msg=r_msg.decode()
            print("")
            print("Recieved Message from client: "+ r_msg+ "")

t1=send()
t2=recieve()
t1.start()
t2.start()