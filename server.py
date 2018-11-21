import chat
import json
import time
import Pyro4
import threading
import socket as sk
import pickle
import os
import time
from utils import *

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

UploadDir = os.path.join(os.getcwd(),os.path.join('Servidor',''))
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
			chat_p = chat.Chat(name=chat_p)
			self.register(chat_p)
		elif chat_p is None:
			chat_p = chat.Chat()
			self.register(chat_p)
		elif isinstance(chat_p, chat.Chat):
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
		global Usuarios,arquivos_em_transferencia,UploadDir
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
				
			elif mensagem[:6] =='login:':
				usersenha=mensagem.replace('login:','')
				usersenha = usersenha
				existe = False
				for i in Usuarios:
					print(i,usersenha)
					if i == usersenha:
						existe = True
				if existe:
					con.send('ok'.encode('utf-8'))
				else:
					con.send('nok'.encode('utf-8'))
			con.close()
	def create_chat(self, chat_name):
		self.lobby.register(chat_name)

if __name__=="__main__": 
	server = Server()
	server.create_chat('Sala')
	server.create_chat('Familia')
	server.create_chat('Test')
	server.create_chat('_1_')
	server.run()

	#keeping server alive
	while True:
		time.sleep(30)
