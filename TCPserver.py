import socket
import time
import sys



class Server:
    SERVER_IP_ADDRESS = "127.0.0.1"
    SERVER_PORT_NO = 6789

    def __init__(self):
        print("Starting TCP server on ({0}: {1})".format(self.SERVER_IP_ADDRESS, self.SERVER_PORT_NO))
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSock.bind((self.SERVER_IP_ADDRESS, self.SERVER_PORT_NO))
        self.serverSock.listen(5)
        self.conn = None
        self.client_addr = None
        try:
            self.conn, self.client_addr = self.serverSock.accept()
        except:
            sys.exit()

    def catch(self):
        try:
            data = self.conn.recv(1024)
        except ConnectionResetError:
            sys.exit()
        if data:
            stop = time.time()
            msg = data.decode("ASCII")
            print("{0} messaged {1} characters at time {2}".format(self.client_addr, str(len(msg)), stop))
            return stop
        else:
            return False

    def reply(self, message):
        self.conn.sendall(message.encode("ASCII"))

if __name__ == '__main__':
    S = Server()
    while True:
        stop = S.catch()
        if stop:
            message = str(stop)
            S.reply(message)
        else:
            break
    S.serverSock.close()




    #_______________
