# Chat-Server
Its a chat server using Socket Library of Python, which deals with instant messaging when server and client are connected/online.

## Libraries used: -

```python
import socket
from threading import Thread
```
Socket library is a low level networking interface, it is a key part of this project.
And threading library is used to send/recieve more than one message at a time.

## How the code works: -

### Socket address: -
Its is really important to add a perfect address which your system is comfortable with,
as here i have used "AF_INET" which is a address, it is safest indeed!

And ".SOCK_STREAM" is used to indicate the type od socket here it is TCP(Transmission Control Protocol).

* Here I have used a localhost server which is almost free.

### Port number: -

Port number is to listen on(non-privileged ports are > 1023), Port number can be iamgined as IP address.

### Bind: -

Bind() is used to associate the socket with a specific network interface and port number.

### How client and server gets connected?

As the client provides the Host IP address here localhost and port number.
so, the server accepts the request and gets connectes with a notification.

### SEND and RECIEVED: -

* How the message is sent/recieved?
A thread argument is passed which helps us to have more than one message at a time.
A while loop is runing with a true condition, message is take as input and it is encoded, and then just sent,
the client/server recieves the message decodes it and prints, along with a notification of message sent or message recieved.

* Note: - Here we are limmiting our message size upto 1024(1MB), can be edited according to need.

At last thread starts, if both server and client are connected.

## Application: -

It is used as a Chating unit, we can have a chat from one PC to another if they are connected with same server.
