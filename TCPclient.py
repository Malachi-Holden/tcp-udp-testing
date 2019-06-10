import socket
import time
import sys

class Client:

    print("starting client")
    SERVER_IP_ADDRESS = "127.0.0.1"
    SERVER_PORT_NO = 6789
    outputfile = "TCPresults_XPS.txt"

    def __init__(self):

        self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.clientSock.connect((self.SERVER_IP_ADDRESS, self.SERVER_PORT_NO))
        except:
            sys.exit()


    def ping(self, message):
        start = time.time()
        msg = message.encode("ASCII")
        self.clientSock.sendall(msg)
        return start

    def catch(self):

        data = self.clientSock.recv(1024)
        msg = data.decode("ASCII")

        stop = float(msg)
        return stop

    def run(self, message):
        start = self.ping(message)
        stop = self.catch()
        duration = stop - start

        return duration

if __name__ == '__main__':
    f = open("TCPresults_XPS.txt", 'w')
    results = ""
    start = time.time()
    C = Client()
    n = int(sys.argv[1])
    if len(sys.argv) >=2:
        m = int(sys.argv[2])
    else:
        m = n

    totaltime = 0
    for i in range(n,m+1):
        message = "x"*i
        duration = C.run(message)
        totaltime += duration
        doc = "{0} characters took {1} seconds\n".format(str(len(message)), str(duration))
        results += doc
        if (i==m) or (i==n):
            print(doc)
    print("average transmission time is {} seconds".format(totaltime/(m-n+1)))
    f.write(results)
    f.close()
    C.clientSock.close()
    stop = time.time()
    print("total time (including setup) was {} seconds".format(stop-start))
