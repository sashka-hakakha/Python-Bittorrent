import bencodepy
import hashlib
import btdht
import binascii
from time import sleep
from socket import *
class Client:
	def __init__(self,torrent):
		self.torrent=torrent
		self.info_hash = get_info_hash(self)
		self.protocol_id = "BitTorrent protocol"
		self.peer_id = "pigeon"
		self.reserved_area = "\x00"*8
	def get_info_hash(self):
		
		f = open(self.torrent,"rb") 
		decoded = bencodepy.decode(f.read())
		#encode torrent info
		info = bencodepy.encode(dict(decoded.get(b"info"))) 
		info_hash = hashlib.sha1(info).hexdigest() 
		print("info hash = " + info_hash)
		return info_hash
	def get_peers(self,torrent):

	#build dht
		dht = btdht.DHT() 
		dht.start() 
		sleep(15) # wait for the DHT to build
	
		none = True
		while none: 
			peers = dht.get_peers(binascii.a2b_hex(self.info_hash))
			print(peers)
			sleep(1)
			if peers != None:
				none = False
		return peers
	def get_handshake_message(self)
		return "".join([chr(len(self.protocol_id)), self.reserved_area,self.info_hash, self.peer_id])
#connecting to peers
def connect_to_peer(peers):
	s = socket(AF_INET, SO_REUSEADDR)
	peer = peers[0][0]
	port = peers[0][1]
	s.connect((peer,port))
	s.close()

peers = get_peers("debian.torrent")
connect_to_peer(peers)