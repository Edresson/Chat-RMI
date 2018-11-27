#import chat
import json
import time
import Pyro4
import threading
import socket as sk
import pickle
import os
import time
from utils import *
from GuiServer import *
from PyQt5 import QtCore, QtGui, QtWidgets
Banidos = []
Conectados =[]
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Chat():
	def __init__(self, name=None):
		self._name = name
		self.messages = []
		self.users = {}
		self.usernames = []

	def connect(self, uri):
		"""Method for remote uses to call when wants to connect to this chat."""
		global ui
		#the client uri is passed so it's methods can be called later.
		client = Pyro4.Proxy(uri)

		#If username taken or uri already in the chat -> quit.
		if uri in self.users or client.username in self.usernames:
			return False

		print(f"O cliente '{client.username}'<- entrou no grupo.")
		item = client.username
		if item not in Conectados:
			Conectados.append(item)
			ui.lista_onlines.clear()
			
			for item in Conectados:
				ui.lista_onlines.addItem(item)

		self._send_message(f'{client.username}<- entrou no grupo.')

		#adding client to chat's users
		self.users[uri] = client
		self.usernames.append(client.username)

		if len(self.messages) < 21:
			return self.messages
		return self.messages[-20:]

	def disconnect(self, uri):
		"""Method for remote uses to call when wants to disconnect from this chat."""
		print(f"{self.users[uri].username}, disconectou-se")
		self._send_message(f"O usuario ->{self.users[uri].username}<- disconectou-se do grupo.", uri)
		item = self.users[uri].username
		Conectados.remove(item)
		ui.lista_onlines.clear()
		for item in Conectados:
			ui.lista_onlines.addItem(item)

		

		#clearing the data:
		self.usernames.remove(self.users[uri].username)
		del(self.users[uri])

	def send_message(self, message, uri):
		global ui,Banidos
		#if the uri is unknown, the message must not be sent
		if uri not in self.users:
			return

		if message [:len('___toban,')] == '___toban,':
			print('recebeu checando banido:',message )
			_,user = message.split(',')
			if user == self.users[uri].username :
				if  user in Banidos:
					self._send_message(message+',y', uri)
				else:
					self._send_message(message+',n', uri)
				return
			else:
				return 
		
		elif message[:9] != 'O Usuario':

			#if the uri doesn't fits the username, someone is pretending to be someone else.
			sender = message.split(':')[0]
			if sender != self.users[uri].username:
				return
		
		ui.lista_logs.addItem(self.name+'-->'+message)
		#actually sending message.
		self._send_message(message, uri)

	def _send_message(self, message, uri=None):
		"""Method invisible for remote users due to starting with '_'.
		register the message and sends to every user connected.

		If it's a system message and must be sent to everybody, no uri is provided."""
		self.messages.append(message)
		for user_uri, user in self.users.items():
			if user_uri == uri: 
				if message [:len('___toban,')] != '___toban,':
					continue
			user.incoming_message(message)
	
	def __str__(self):
		return f"chat named {self.name}"

	@property
	def name(self):
		return self._name

class Lobby():
	def __init__(self, hostname='localhost', port=25501):
		"""hostname : str (default='localhost') - address which the daemon should run.
		- port : int (default=25501) - port which the daemon should run.
		- logs chats and hosts it. use 'register' to create new chats."""
		self.chats = []
		self.daemon = Pyro4.Daemon(host=hostname, port=port)

	def daemon_loop(self):
		"""Starts the daemon"""
		self.d_thread = threading.Thread(target=self.daemon.requestLoop)
		self.d_thread.daemon = True
		self.d_thread.start()


	def register(self, chat_p=None):
		"""Logs a new chat to the daemon and hosts it.
		- chat_p : None - A nameless chat is created and hosted.
		- chat_p : str - creates a chat named as {chat_p} and registers it.
		- chat_p : chat.Chat - registers the chat."""
		if isinstance(chat_p, str):
			chat_p = Chat(name=chat_p)
			self.register(chat_p)
		elif chat_p is None:
			chat_p = Chat()
			self.register(chat_p)
		elif isinstance(chat_p, Chat):
			uri = str(self.daemon.register(chat_p))
			self.chats.append((chat_p.name, uri))

class Server():
	def __init__(self, hostname='localhost', port=25500, lobby_port=25501):
		"""This class works as a DNS server for the chats.
		- hostname : str (default='localhost') - address which the server should run.
		- port : int (default=25500) - port which the server should run.
		- lobby_port : int (default=25501) - port which the daemon should run."""

		print("Setting up daemon")
		self.lobby = Lobby(hostname=hostname, port=lobby_port)
		self.lobby.daemon_loop()

		print("Setting up server")
		self._server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
		self._server.bind((hostname, port))

	def run(self):
		self.s_thread = threading.Thread(target=self._run)
		self.s_thread.daemon=True
		self.s_thread.start()

	def _run(self):
		global Usuarios,arquivos_em_transferencia,UploadDir,ui
		print("Running server")
		self._server.listen()

		while True:
			con, _ = self._server.accept()
			mensagem = con.recv(2048).decode('utf-8')
			comando = mensagem
			if mensagem == 'GET uri':
				con.send(json.dumps(self.lobby.chats).encode())

			elif comando[:9] =='download:':
				print('Iniciando download:') 
				usuario,comando= comando.replace('download:','').split(':')
				
				arquivo = os.path.join(UploadDir ,comando)
				#Bytes in Test File7
				print('Arquivo: ',arquivo)
			
				numBytesFile = determine_num_bytes(arquivo)

				#Opening the test file
				testFileObj = open_text_file(os.path.abspath(arquivo))
				arquivopath = arquivo.replace(UploadDir,'')#usado para poder upar pastas
				#Read the text file to the socket
				read_text_file(con, testFileObj, numBytesFile,arquivopath)

				#serverResponse = sock.recv(1024)
				#print "Server received <" + str(serverResponse) + "> bytes."
				#Closing the test file
				testFileObj.close()

			elif comando[:7] == 'upload:':
				print('Fazendo Upload')
				filename = comando.replace('upload:','')
				print(filename)
				#filename = filename.decode('utf-8')
				con.send('ok'.encode('utf-8'))
				
				filename= os.path.join(UploadDir,filename)
				print(filename)
				if not os.path.exists(os.path.dirname(filename)):
					try:
						os.makedirs(os.path.dirname(filename))
					except OSError as exc: # Guard against race condition
						pass
				file = open(filename, "w+")
				#get the first line of the file
				clientInput = con.recv(1024).decode('utf-8')
				bytesReceived = 0

				#for each line the client sends, add it to the transf
				while clientInput != "\r\n\r\n" and clientInput != "":
					bytesReceived += len(clientInput)
					file.write(clientInput)
					clientInput = con.recv(1024).decode('utf-8')
				

				if(clientInput == "" or clientInput == "\r\n\r\n"):
				#needs to have the double \\ to cancel out interpreting it as a string
					
					con.send(str(bytesReceived).encode('utf-8'))
					file.close()
					con.close()
				time.sleep(2)

			elif mensagem[:11] =='createuser:':
				usersenha=mensagem.replace('createuser:','')
				user,_=usersenha.split(':')
				userexiste = False
				print(Usuarios)
				for i in Usuarios:
					print(i[:len(user)], user)
					if i[:len(user)]== user:
						userexiste = True
				if userexiste:
					con.send('nok'.encode('utf-8'))
				else:
					Usuarios.append(usersenha)
					saveusers()
					con.send('ok'.encode('utf-8'))
			elif mensagem[:11] =='createchat:':
				msg=mensagem.replace('createchat:','')
				self.lobby.register(msg)#create chat
				ui.lista_grupos.addItem(msg)
				
			elif mensagem[:6] =='login:':
				usersenha=mensagem.replace('login:','')
				usersenha = usersenha
				existe = False
				for i in Usuarios:
					print(i,usersenha)
					if i == usersenha:
						existe = True
				
				if existe:
					banido = False
					for i in Banidos:
						if i == usersenha.split(':')[0]:
							banido =True
							
					if banido == True:
						con.send('ban'.encode('utf-8'))
					else:
						con.send('ok'.encode('utf-8'))
						if usersenha.split(':')[0] not in Conectados:
							Conectados.append(usersenha.split(':')[0])
							ui.lista_onlines.clear()
							for i in Conectados:
								ui.lista_onlines.addItem(i)
							
				else:
					con.send('nok'.encode('utf-8'))

			elif  mensagem[:6] =='toban:':
				
				_,user=mensagem.split(':')
				print('recebeu checkban: ',user)
				if  user in Banidos:
					con.send('ban'.encode('utf-8'))
				else:
					con.send('nban'.encode('utf-8'))
			
			con.close()

	def create_chat(self, chat_name):
		global ui
		self.lobby.register(chat_name)
		ui.lista_grupos.addItem(chat_name)

### GUI functions		
def irgrupos():
	global ui 
	ui.stackedWidget.setCurrentIndex(0)

def irlogs():
	global ui 
	ui.stackedWidget.setCurrentIndex(1)

def irconfig():
	global ui 
	ui.stackedWidget.setCurrentIndex(2)

def startserver():
	global ui,server 
	ui.bt_start.setEnabled(False)
	ui.bt_parar.setEnabled(True)
	
	server_ip=ui.server.text()
	port_lobby=int(ui.lobby_port.text())
	port =int(ui.port.text())
	server = Server(hostname=server_ip, port=port, lobby_port=port_lobby)
	ui.lista_grupos.clear()
	defaultschats = [ 'Sala','Familia','Memes']
	for i in defaultschats:
		server.create_chat(i)

	server.run()

def stopserver():
	global server,ui
	ui.bt_start.setEnabled(True)
	ui.bt_parar.setEnabled(False)
	del server

def criargrupo():
	global ui,server
	gruponame=ui.gruponame.text()
	server.create_chat(gruponame)

def clearlogs():
	global ui
	ui.lista_logs.clear()
	
if __name__=="__main__": 
	
	try:
		with open('Usuarios.list', 'rb') as fp:
			Usuarios = pickle.load(fp)
	except:
		Usuarios = [] 
		with open('Usuarios.list', 'wb') as fp:
			pickle.dump(Usuarios,fp)

	def saveusers():
		global Usuarios
		with open('Usuarios.list', 'wb') as fp:
			pickle.dump(Usuarios,fp)

	def baniruser():
		global ui,Banidos,Conectados
		try:
			user=str(ui.lista_onlines.currentItem().text())
		except:
			return 0	
		'''item = ui.lista_onlines.findItems(user, QtCore.Qt.MatchRegExp)[0]
		item.setSelected(False)'''
		Conectados.remove(user)
		ui.lista_onlines.clear()
		for item in Conectados:
			ui.lista_onlines.addItem(item)

		
		

		Banidos.append(user)
		#ui.lista_banidos.addItem(user)
		ui.lista_banidos.clear()
		for item in Banidos:
			print('item adicionado nos banidos',item)
			ui.lista_banidos.addItem(item)
		#ui.lista_onlines.clearSelection()
		'''ui.lista_onlines.setEnabled(False)
		ui.lista_banidos.setEnabled(False)
		ui.lista_onlines.setEnabled(True)
		ui.lista_banidos.setEnabled(True)'''
		ui.lista_banidos.setEnabled(False)
		ui.lista_onlines.setEnabled(False)
		time.sleep(3)
		ui.lista_onlines.setEnabled(True)
		ui.lista_banidos.setEnabled(True)

		
	def desbaniruser():
		global ui,Banidos,Conectados
		try:
			user=str(ui.lista_banidos.currentItem().text())
		except:
			print('Excessão no desbanir user')
			return 0
		
		#ui.lista_onlines.addItem(user)
		Banidos.remove(user)
		print('item removido dos banidos',user)
		ui.lista_banidos.clear()
		for item in Banidos:
			ui.lista_banidos.addItem(item)
		
		#ui.lista_banidos.clearSelection()
		'''ui.lista_onlines.setEnabled(False)
		ui.lista_banidos.setEnabled(False)
		ui.lista_onlines.setEnabled(True)
		ui.lista_banidos.setEnabled(True)'''
		
		


	UploadDir = os.path.join(os.getcwd(),os.path.join('Servidor',''))
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	
	server = 0
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.ir_grupos.clicked.connect(irgrupos)
	ui.ir_grupos_2.clicked.connect(irgrupos)
	ui.ir_logs.clicked.connect(irlogs)
	ui.ir_logs_2.clicked.connect(irlogs)
	ui.ir_config_2.clicked.connect(irconfig)
	ui.ir_config.clicked.connect(irconfig)
	ui.bt_start.clicked.connect(startserver)
	ui.bt_parar.clicked.connect(stopserver)
	ui.bt_parar.setEnabled(False)
	ui.bt_criargrupo.clicked.connect(criargrupo)	
	ui.bt_limpar_logs.clicked.connect(clearlogs)
	ui.lista_onlines.currentItemChanged.connect(baniruser)
	ui.lista_banidos.currentItemChanged.connect(desbaniruser)
	MainWindow.setWindowTitle("Servidor")
	MainWindow.show()
	sys.exit(app.exec_())




