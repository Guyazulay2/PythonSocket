import socketserver, subprocess, sys
from threading import Thread
from pprint import pprint
import json

HOST = '0.0.0.0'
PORT = 5600

class SingleTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        text = data.decode('utf-8')
        print(text)
        datatosend = ''
        with open("data.json",'r') as f:
            j = json.load(f)
            datatosend = json.dumps(j)

        self.request.send(bytes(datatosend, 'UTF-8'))
        self.request.close()

class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":
    server = SimpleServer((HOST, PORT), SingleTCPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
