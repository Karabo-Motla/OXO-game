from datetime import *
from socket import *
from GameIni import *

# Basic networking and log(logfile) functionality

class GameClient:
    
    def __init__(self):
        self.log_file = open(GAME_NAME + 'GameClient.log','w')
        self.log_file.close()
        self.log(GAME_NAME + ' Game Client Started: ' + str(datetime.now()))
        self.socket = socket(AF_INET, SOCK_STREAM)    # Create a socket object for TCP/IP communication

    # Connect to the server using the provided host and predefined port    
    def connect_to_server(self,host):
        self.socket.connect((host, PORT))
        self.log('Connected To Server: ' + str(host))

    # Send a message to the server, formatted and encoded    
    def send_message(self,msg):
        self.socket.send(BUFFER_STR.format(msg).encode())
        self.log('Sent Message: ' + msg)
    
    # Receive a message from the server, decode and strip any extra spaces
    def receive_message(self):
        msg = self.socket.recv(BUFFER_SIZE).decode().strip()
        self.log('Received Message: ' + msg)
        return msg 

    # Log a message to the log file with a timestamp    
    def log(self,msg):
        self.log_file = open(GAME_NAME + 'GameClient.log','a')
        self.log_file.write(msg + '\n')
        self.log_file.close()

    # Close the socket and log the end message when the object is deleted    
    def __del__(self):
        self.socket.close()
        self.log(GAME_NAME + ' Game Client Ended: ' + str(datetime.now()))
