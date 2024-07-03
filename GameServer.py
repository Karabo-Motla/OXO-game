import sys
from datetime import *
from socket import *
from GameIni import *

# Basic networking and output(screen and logfile) functionality

class GameServer:
    
    def __init__(self):
        self.log_file = open(GAME_NAME + 'GameServer.log','w')
        self.log_file.close()
        self.output(GAME_NAME + ' Game Server Started: ' + str(datetime.now()))
        self.socket = socket(AF_INET, SOCK_STREAM)     # Create a socket object for TCP/IP communication

        # Bind the socket to the address and port, and start listening for connections
        self.socket.bind(('', PORT))            
        self.socket.listen(2)


    # Accept connections from two clients
    def accept_clients(self):
        self.clients = []
        self.output('Waiting for client connections.')
        self.clients.append(self.socket.accept())
        self.output('Connected Client 0: ' + str(self.clients[0][1]))
        self.clients.append(self.socket.accept())
        self.output('Connected Client 1: ' + str(self.clients[1][1]))
    
    # Send a message to the specified client, formatted and encoded
    def send_message(self,i,msg):
        self.clients[i][0].send(BUFFER_STR.format(msg).encode())
        self.output('Sent Message Client ' + str(i) + ': ' + msg)

    # Receive a message from the specified client, decode and strip any extra spaces
    def receive_message(self,i):
        msg = self.clients[i][0].recv(BUFFER_SIZE).decode().strip()
        self.output('Received Message Client ' + str(i) + ': ' + msg)
        return msg
    
    # Close connections to both clients and clear the client list
    def close_clients(self):
        self.clients[0][0].close()
        self.output('Closed Client 0: ' + str(self.clients[0][1]))
        self.clients[1][0].close()
        self.output('Closed Client 1: ' + str(self.clients[1][1]))
        self.clients = []

    # Print a message to the screen and log it to the log file    
    def output(self,msg):
        print(msg + '\n')
        sys.stdout.flush()
        self.log_file = open(GAME_NAME + 'GameServer.log','a')
        self.log_file.write(msg + '\n')
        self.log_file.close()


    # Clean up resources by closing the socket and logging the shutdown of the game server when the object is deleted    
    def __del__(self):
        self.socket.close()
        self.output(GAME_NAME + ' Game Server Ended: ' + str(datetime.now()))
