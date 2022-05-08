from socket import *
class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = None
        self.choking = True
        self.interested = False
    def __str__(self):
        return "ip: " + str(self.ip) + " port: " + str(self.port)
    """
    def has_piece(self, i):
            return self.bits[i]
	        
		except:
			print("could not connect to peer")
		try:
			self.s.sendall(self.torrent.get_handshake_message())                except:
                        print("could not send handshake to peer")
        def send(self, data):
            try:
                self.s.send(data)
            except:
                print("could not send to peer")
        def set_unchoked(self):
            self.choking = False
        def check_choking(self):
            return self.choking
        def check_interested(self):
            return self.interested
        def check_choking(self):
            return self.choking
class Peer_Manager():
    def __init__(self, client, piece_manager):
        self.piece_manager = piece_manager
        self.peers = []
        self.client = client
    def get_peer_with_piece(self, i):
        for peer in peers:
            if peer.has_piece and not peer.choking:
                return peer
    def has_unchoked(self):
        for peer in self.peers:
            if peer.choking = False
                return True
        return False
"""
