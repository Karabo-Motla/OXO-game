from GameClient import *

class OXOTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE
        
    def input_server(self):
        return input('enter server:')
     
    def input_move(self):
        return input('enter move(0-8):')
     
    def input_play_again(self):
        return input('play again(y/n):')

    def display_board(self): # method for displaying empty board
        print(self.board[0],"|",self.board[1],"|",self.board[2],"|","           0  |","  1  |","  2  |")
        print(self.board[3],"|",self.board[4],"|",self.board[5],"|","           3  |","  4  |","  5  |")
        print(self.board[6],"|",self.board[7],"|",self.board[8],"|","           6  |","  7  |","  8  |")
    
    
    def handle_message(self,msg):
        if msg[:msg.find(",")]=="new game":   #checks if the first sliced part of the message is new game
            print("New game! Your character is",msg[-1])  #tells user their character
            self.display_board()   #displays board
        elif msg=="your move":                    #checks if message is your move
            print("It's your turn to play!")      #tells client that it is the turn
            move=self.input_move()                #assigns client's move to a variable
            self.send_message(move)               #sends client's move to the server
        elif msg=="opponents move":               #checks if message is opponents move     
            print("It's your opponents turn")     #informs the client that their opponent should make their move
        elif msg[:msg.find(",")]=="valid move":   #checks if the first sliced part of the message is valid move
            self.shape=msg[-3]                    #receives client's shape from message
            position=int(msg[-1])                 #receives client's move position from message
            self.board[position]=self.shape       #updates board with client's shape 
            self.display_board()                  #displays updated board
        elif msg=="invalid move":                 #checks if message is invalid move
            print("Your move in invalid...Please play again.")  
        
        elif msg=="game over,T":
            print("GAME OVER!! It's a tie")
            
        elif msg[:msg.find(",")]=="game over":   #checks if the first sliced part of the message is game over
            self.shape==msg[-1]                  #receives shape of the winner from the message
            if self.shape=="X" or self.shape=="O":            #checks for the shape of the winner
                print("GAME OVER!! Player",self.shape,"won")
        
        elif msg=="play again":                   #checks if message is play again
            response=self.input_play_again()      #receives client's response
            self.send_message(response)           #sends response to the server
            if response=="y":
                self.clear_board()                #clears the board if user decides to play again
            else:
                print("Thank you for playing...GOODBYE :)")   
        elif msg=="exit game":
            print("Game has been ended.")
            
    
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            else: break
            
def main():
    otc = OXOTextClient()
    while True:
        try:
            otc.connect_to_server(otc.input_server())
            break
        except:
            print('Error connecting to server!')
    otc.play_loop()
    input('Press click to exit.')
        
main()