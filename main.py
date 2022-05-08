import sys
from client import Client
from tracker import Tracker

def handshake(s, self_name, peer_id, info_hash):
    self_name = self_name.encode('utf-8')
    self_name_length = bytes([len(self_name)])
    handshake = self_name_length + self_name + bytes(8) + info_hash + peer_id
    s.send(handshake)

    try:
        recieved = s.recv(68)
        while(len(rcv) < 68):
            recieved = s.recv(68-len(recieved))
    except:
        return False
    
    #success if length of recieved handshake is correct
    return len(recieved) == 68




if __name__ == "__main__":
    filename = sys.argv[1]

    client = Client(filename)
    tracker = Tracker(client)
    tracker.run()
