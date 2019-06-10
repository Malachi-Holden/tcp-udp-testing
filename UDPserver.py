import socket
import time


class Server:
    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = 6789
    followupaddress = "127.0.0.1"
    followupport = 6790

    def __init__(self):

        print("starting UDP server on ({0}: {1})".format(self.UDP_IP_ADDRESS, self.UDP_PORT_NO))
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.bind((self.UDP_IP_ADDRESS, self.UDP_PORT_NO))
        self.followupclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def catch(self):
        data, addr = self.serverSock.recvfrom(1024)
        stop = time.time()
        msg = data.decode("ASCII")
        print("{0} messaged {1} characters at time {2}".format(addr, str(len(msg)), stop))
        return stop

    def reply(self, message):
        self.followupclient.sendto(message.encode("ASCII"), (self.followupaddress, self.followupport))

if __name__ == '__main__':
    S = Server()
    while True:
        stop = S.catch()
        message = str(stop)
        S.reply(message)




    #_______________
