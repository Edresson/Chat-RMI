# RMI-Chat
Chat coded in python using RMI and sockets

Programming language: Python 3.7.0

Used libraries:
	- json
	- time
	- socket
	- threading
	- pyqt5
	- Pyro4


run using: python3.7 client.py

Pyro4 and tkinter might not come with your python version, depending on the operation system and/or python distribution.

The program consists in 2 files:
	- server.py - responsable for creating a 'dns server' to locate the uri and start the chat rooms.
	- client.py - responsable for discovering the existing chats in the server and connecting the user to the chat room, contains the 'User' class which will create a GUI and interact with the chatroom via RMI and contains the 'Chat' class which manages the interations between the connected users.


