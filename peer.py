from socket import *
class Peer:
	def __init__(self, ip, port,client):
		self.ip = ip
		self.port = port
		self.client = client
	def get_ip(self):
		return self.ip
	def get_port(self):
		return self.port
	def run(self):
		self.s = socket(AF_INET, SO_REUSEADDR)
		self.s.settimeout(10)
		try:
			self.s.connect((self.ip,self.port))
		except:
			self.s.close()
		try:
			self.s.sendall(self.torrent.get_handshake_message())
