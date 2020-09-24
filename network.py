import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket(socket .AF_INET, socket.SOCK_STREAM)
        self.server = '' // Here you put your server
        self.port = 4444
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP():
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client(recv(2048).decode)()
        except:
            pass

     def send (self, data):
         try:
             self.client.send(str.encode(data))
             return pickle.loads(self.client(recv(2048*2))
        except:
            socket.error as e:
                print(e)
