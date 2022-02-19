# README
## TLDR
The server relays messages from a user to all users, the client has a GUI and can receive and send messages to the server.

## Introduction
This project will consist of two parts:

- The server which is the central storage for messages, which main function is to relay messages to all connected clients.
- The client which receives messages from the server and sends messages to all clients connected to the server. The client will also have a wxpython graphical user interface (GUI).

This project will be developed completely using test-driven development (TDD). This is the first time I apply TDD to a project and this project is meant to learn TDD.

## Requirements
### Server requirements
The server should be able to have up to *n* clients connected at once. Each client should have its own `multiprocessing` process for receiving messages and for sending messages in the server application. The server sends messages to clients on port 6969, and receives messages from clients on port 6970. The server contains a messages list. Every time a new message is received, it will be appended to the message list and a flag will be set. The sender processes of all the clients at the server side will respond to this flag by pickling the data in the messages list, hashing the pickled object, and sending first the hash to the clients followed by the pickle data. The clients can then check the hash with the pickled data, and if it matches, unpickle the data and update the messages list. The clients can then sort the messages list in a separate `multiprocessing` process.

### Client requirements
When the client is started, it should show a prompt asking for the IP-address of the server they want to connect to and the username they want to use. After that it should show a GUI containing a big textfield showing all messages, and a small textfield under that which can be used to send messages. This can be seen in the image below:
![Client layout](./doc/images/client_layout.png)

## Milestones
