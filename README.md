OXO Game Project
Overview
The OXO Game Project is a multiplayer Tic-Tac-Toe (also known as Noughts and Crosses) game implemented using Python. The game consists of a client-server architecture, with the server handling multiple clients.
The clients communicate with the server to update the game state and display the board in a GUI. The GUI is built using PyQt5, which provides a user-friendly interface for players.

Features
-Multiplayer support via client-server architecture
-Real-time communication between server and clients
-Graphical User Interface (GUI) built with PyQt5
-Logging of game events for debugging and record-keeping
-Signal handling to update the GUI based on game events
-Dynamic board updates to reflect player moves

Project Structure
GameIni.py: Contains game-specific constants like GAME_NAME, PORT, BUFFER_SIZE, BUFFER_STR, and BOARD_SIZE.
GameClient.py: Implements the client-side logic for connecting to the server, sending and receiving messages, and logging events.
GameServer.py: Implements the server-side logic for accepting client connections, handling communication, and logging events.
LOOP.py: Extends QThread and GameClient to manage continuous communication and updates between the client and server.
OXO.py: The main entry point of the application, initializing and running the game server and clients.


Running the Game
1.Start the Game Server:
>>python GameServer.py

2.Open the GUI in oxo.py on two separate IDEs:

Run the following command in two separate IDEs or open one GUI then use command prompts for the other client:
>>python oxo.py

Network Configuration
Localhost: When running the game on the same machine, use localhost as the IP address.
Multiple Machines: If using two machines, use the IP address of the machine running the server.


How to Play
The game supports two players (X and O).
The server accepts connections from two clients.
Players take turns making moves by clicking on the buttons in the GUI.
The game detects and announces the winner when a player gets three of their marks in a row (horizontally, vertically, or diagonally).
The game state is displayed on the GUI, and the board is updated dynamically.
