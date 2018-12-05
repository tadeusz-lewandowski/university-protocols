from config import BUFFER_SIZE

class Messanger:
	def __init__(self, socket):
		self.socket = socket
	def get_message(self):
		return self.socket.recv(BUFFER_SIZE)
	def send_message(self, message):
		self.socket.send(message)