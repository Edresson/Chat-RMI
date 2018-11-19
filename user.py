import Pyro4
import tkinter
import threading
import sys
from Gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction
import socket as sk
import json
def get_uris(server, port):
	'''Função que se conecta ao servidor \"dns\" de uri
	e descobre quais são os chats existentes'''
	socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
	socket.connect((server, port))

	socket.send('GET uri'.encode())

	serialized = socket.recv(4096).decode('utf-8')

	return json.loads(serialized)

def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class User():
	#@threaded
	def __init__(self, uri, username,server,port):
		"""The instantiation of this class requires:
			- uri : str - uri to connect to chat.
			- username : str - how it shall be displayed for the participants in the chat."""
		print('start init')
		self.server = server
		self.port = port
		self.chat = Pyro4.Proxy(uri)
		self._username = username
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		app.aboutToQuit.connect(self.closeEvent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(MainWindow)
		self.ui.sendbtn.clicked.connect(self.send_message)
		self.ui.grupos.clear()
		uris = get_uris(server, port)
		for line in uris:
			self.ui.grupos.addItem(line[0])

		self.ui.grupos.currentTextChanged.connect(self.changegroup)
		
		#Creating daemon so the chat can access this object.
		self.daemon = Pyro4.Daemon()
		#try:
		self._my_uri = self.daemon.register(self)
		#On closing
		#self.top.protocol("WM_DELETE_WINDOW", self.disconnect) #trocar para qt

		self.connect()

		
		try:
			MainWindow.show()
			sys.exit(app.exec_())
			#tkinter.mainloop()
		except Exception as e:
			print(e)
			self.disconnect()

	def closeEvent(self):
		self.disconnect()

	def changegroup(self, value):
		try:
			self.disconnect()
		except:
			return 0
		uris = get_uris(self.server, self.port)
		#self.ui.grupos.clear()
		
		selection = 0
		
		for i in range(len(uris)):
				#print(uris[i])
				if uris[i][0] == value:
					selection = i
				#self.ui.grupos.addItem(uris[i][0])
		
		

		uri = uris[int(selection)][1]
		print(uri)
		print('chamou')
		self.daemon.unregister(self)
		del self.daemon
		del self.chat
		del self._my_uri
		self.chat = Pyro4.Proxy(uri)
		#self.chat = Pyro4.Proxy(uri)
		
		#Creating daemon so the chat can access this object.
		self.daemon = Pyro4.Daemon()
		#try:
		self._my_uri = self.daemon.register(self)
		self.connect()
		print("combobox changed", value)


	def connect(self):
		"""Method to connect and register at the chat"""

		print('Connecting to server')
		'''except:
			print('unregistred')
			self.daemon.unregister(self)
			print('registrando')
			self._my_uri = self.daemon.register(self)'''

		self.t = threading.Thread(target=self.daemon.requestLoop)
		self.t.daemon = True
		self.t.start()

		messages = self.chat.connect(self.my_uri)

		#in case the connection is refused:
		if isinstance(messages, bool) and not messages:
			raise ValueError(f"Username {self.username} already taken")

		print('Connected')

		#if the connection is accepted, the last 20 messages are sent
		#those messages will now be printed.
		for message in messages:
			self.incoming_message(message)
	

	def disconnect(self):
		"""This method closes the window and clears the username in the chat."""
		self.ui.chatlist.clear()
		#self.top.quit()
		self.chat.disconnect(self.my_uri)
	
		print('Disconnected')

	def send_message(self, message=None):
		#Getting message from window, clearing then sending to server
		message = self.ui.linesend.text()
		self.ui.linesend.setText("")
		message = f"""{self.username}: {message}"""

		self.chat.send_message(message, self.my_uri)

		#as the chat can't call methods from this object when it's called,
		#it must be printed by itself
		self.incoming_message(message)

	def incoming_message(self, message):
		#Recieving a message -> displaying at window.
		self.ui.chatlist.addItem(message)

	def __eq__(self, other):
		return self.username == other.username

	def __str__(self):
		return self._username

	def __repr__(self):
		return self._username

	@property
	def username(self):
		return self._username

	@property
	def my_uri(self):
		return self._my_uri
	
	