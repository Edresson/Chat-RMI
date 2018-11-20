import Pyro4
import tkinter
import threading
import sys
from Gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction
import socket as sk
import json
import hashlib 
import sys
def get_uris(server, port):
	'''Função que se conecta ao servidor \"dns\" de uri
	e descobre quais são os chats existentes'''
	socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
	socket.connect((server, port))

	socket.send('GET uri'.encode())

	serialized = socket.recv(4096).decode('utf-8')

	return json.loads(serialized)

def connect_tcp(server, port):
	socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
	socket.connect((server, port))
	return socket

def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class User():
	#@threaded
	def __init__(self,server='localhost', port=25500):
		"""The instantiation of this class requires:
			- uri : str - uri to connect to chat.
			- username : str - how it shall be displayed for the participants in the chat."""
		print('start init')
		self.server = server
		self.port = port
		
		
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		app.aboutToQuit.connect(self.logout)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(MainWindow)
		self.ui.sendbtn.clicked.connect(self.send_message)
		self.ui.grupos.currentTextChanged.connect(self.changegroup)
		self.ui.grupos.clear()
		#### buttons connections ####
		self.ui.Registrarse.clicked.connect(self.registrar_se) # o botao para ir para pagina de registro
		self.ui.Login.clicked.connect(self.login) # botao de login
		self.ui.Registrar.clicked.connect(self.registrar) # botao de registro
		self.ui.bt_logout.clicked.connect(self.logout)
		self.ui.bt_voltar.clicked.connect(self.voltar_page)
		self.ui.linesend.returnPressed.connect(self.send_message)
		MainWindow.show()
		sys.exit(app.exec_())

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

	def get_login_information(self):
		password = self.ui.Senha.text()
		result = hashlib.md5(password.encode()) 
		senha=result.hexdigest()
		return self.ui.Usuario.text(),senha

	def get_register_information(self):
		password = self.ui.RSenha.text()
		result = hashlib.md5(password.encode()) 
		rsenha=result.hexdigest()
		password = self.ui.confSenha.text()
		result = hashlib.md5(password.encode()) 
		confSenha=result.hexdigest()
		return self.ui.RUsuario.text(),rsenha,confSenha

	def registrar_se(self):
		self.ui.stackedWidget.setCurrentIndex(1)

	def voltar_page(self):
		self.ui.stackedWidget.setCurrentIndex(2) # return for login
	def login(self):
		
		sock = connect_tcp(self.server, self.port)
		usuario,senha=self.get_login_information()
		msg = 'login:'+usuario+':'+senha
		sock.send(msg.encode('utf-8') )
		comando= sock.recv(1024).decode('utf-8')
		comando = comando.replace('\r\n\r\n','')
		if comando == 'ok':
			self._username = usuario
			uris = get_uris(self.server, self.port)
			self.chat = Pyro4.Proxy(uris[0][1])#set initial uri for default
			self.ui.grupos.clear()
			for line in uris:
				self.ui.grupos.addItem(line[0])

			self.ui.stackedWidget.setCurrentIndex(0)
			
			#Creating daemon so the chat can access this object.
			self.daemon = Pyro4.Daemon()
			self._my_uri = self.daemon.register(self)
			
			try:
				self.connect()
			except Exception as e:
				print(e)
				self.disconnect()
		elif comando == 'nok':
			self.ui.label_warning.setText("Senha ou usuario incorreto tente novamente")

	def proxima_page(self):
		self.ui.stackedWidget.setCurrentIndex(3)

	def voltar_page(self):
		self.ui.stackedWidget.setCurrentIndex(2)

	def registrar(self):
		usuario,senha,confsenha=self.get_register_information()
		print(usuario,senha,confsenha)
		if confsenha != senha:
			self.ui.label_warning_create.setText("as senhas não estão iguais")
		if usuario == '' or senha =='' or confsenha == '':
			self.ui.label_warning_create.setText("Preencha todos os campos")
		sock = connect_tcp(self.server, self.port)
		msg = 'createuser:'+usuario+':'+senha
		sock.send(msg.encode('utf-8') )
		comando= sock.recv(1024).decode('utf-8')
		comando = comando.replace('\r\n\r\n','')
		if comando == 'ok':
			self.ui.stackedWidget.setCurrentIndex(2) # return for login
		elif comando == 'nok':
			self.ui.label_warning_create.setText("Esse Usuario já existe faça login !")
	def logout(self):
		try:
			self.disconnect()
		except:
			return 0
		self.daemon.unregister(self)
		del self.daemon
		del self.chat
		del self._my_uri
		self.ui.stackedWidget.setCurrentIndex(2) # return for login

if __name__ == '__main__':
	User()