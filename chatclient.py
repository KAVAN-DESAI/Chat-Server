import socket
from threading import Thread

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host="127.0.0.1"

port=4455
s.connect((host,port))
print("Connected to server: "+ host+ ".")

class send(Thread):
    def run(self):
        while True:
            cli_msg=input("Enter your message: ")
            cli_msg=cli_msg.encode()
            s.send(cli_msg)
            print("")
            print("Your message is sent!")

class recieve(Thread):
    def run(self):
        while True:
            r_msg=s.recv(1024)
            r_msg=r_msg.decode()
            print("")
            print("Recieved message from server: "+ r_msg)

t1=send()
t2=recieve()
t1.start()
t2.start()