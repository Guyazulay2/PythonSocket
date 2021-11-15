import sys
from time import sleep
import socket
import json

HOST , PORT = '127.0.0.1', 8080
data = {
"ssss": "string",
"testt": 10,
"info": "sample is test"
}
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    sleep(2)
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        client.send(bytes(json.dumps(data), 'UTF-8'))

    # Receive data from the server and shut down
        received = json.loads(client.recv(1024).decode('UTF-8'))
    finally:
        client.close()
    print ("Sent: {}".format(data))
    print ("Received: {}".format(received))

