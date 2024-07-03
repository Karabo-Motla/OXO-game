
from GameClient import *  
from time import *  
from PyQt5.QtCore import *  

# Define the LOOP class that inherits from QThread and GameClient

class LOOP(QThread, GameClient):
 
    updating_signal = pyqtSignal(str)  # Define a custom PyQt signal that emits a string
    
    def __init__(self):
        # Initialize both parent classes
        GameClient.__init__(self)
        QThread.__init__(self)
        self.host = ''  # Initialize the host attribute with an empty string
        
    def run(self):
        # Attempt to connect to the server in a loop
        while True:
            try:
                self.connect_to_server(self.host)  # Try to connect to the server
                break  
            except:
                print('Error connecting to server: ')  # Print an error message if connection fails
                self.log('Exception: ')  # Log the exception
                break  # Break the loop if connection fails
        self.play_loop()  # Start the play loop
        
    def play_loop(self):
        # Loop to continuously receive and process messages from the server
        while True:
            msg = self.receive_message()  # Receive a message from the server
            if len(msg):
                self.updating_signal.emit(str(msg))  # Emit the message using the custom signal
            else:
                break  # Break the loop if no message is received
                
    def making_moves(self, mess):
        # Send a message to the server
        self.send_message(mess)
