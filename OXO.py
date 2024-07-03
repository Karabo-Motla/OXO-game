# OXO project
# Karabo Motla
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from GameClient import *
from LoopThread import *
 

        
class OXO_GAME(QWidget,GameClient):
 
    def __init__(self):
        GameClient.__init__(self)
        QWidget.__init__(self)
        self.PlayLoop=LOOP()
        self.setWindowTitle('OXO Game')
        self.setGeometry(100, 100, 600, 400)
        self.resize(600,100)
        self.setStyleSheet('background-color: darkCyan')
        layout = QGridLayout()
        #Labels
        self.server_label=QLabel('Enter server:')
        self.line_edit = QLineEdit()
        self.welcom_label = QLabel(" ") 
        self.connectServer_button = QPushButton('Connect')
        self.welcom_pic = QPixmap("welcoming_pic.png")
        self.front_text=QLabel("TenElevenGames \n     OXO")
        self.front_text.setFont(QFont("Courier",50,3))
        self.startgame_button = QPushButton("Start Game")
        self.startgame_button.setStyleSheet('background-color:grey')
        self.line_edit.setMaximumSize(100,25)
        self.welcom_label.setPixmap(self.welcom_pic)
        self.server_messages=QLabel('Messages from server:\n              \n')
        self.server_messages.setStyleSheet("border: 1px solid black;")
        self.shape_label=QLabel('Your shape:\n      \n')
        self.winner_label=QLabel(" ")
        self.shape_OX = QLabel(" ")
        
        #Push buttons for board game
        self.blankBtn_0=  QPushButton('\n\n')
        self.blankBtn_0.resize(150, 150)
        self.blankBtn_1 = QPushButton('\n\n')
        self.blankBtn_2 = QPushButton('\n\n')
        self.blankBtn_3=  QPushButton('\n\n')
        self.blankBtn_4 = QPushButton('\n\n')
        self.blankBtn_5 = QPushButton('\n\n')  
        self.blankBtn_6=  QPushButton('\n\n')
        self.blankBtn_7 = QPushButton('\n\n')
        self.blankBtn_8 = QPushButton('\n\n') 
        
        #Buttons and layout
        self.play_again=QPushButton('New game')
        self.play_again.setStyleSheet('background-color:green')
        self.quit=QPushButton('Exit')
        self.quit.setStyleSheet('background-color:red')
        self.play_again.clicked.connect(self.new_game)
        self.quit.clicked.connect(self.Quit)
        self.button_layout=QHBoxLayout()
        self.button_layout.addWidget(self.play_again)
        self.button_layout.addWidget(self.quit)
        self.buttonG_layout=QWidget()
        self.buttonG_layout.setLayout(self.button_layout)
        self.button_group=QButtonGroup()
        self.button_group.addButton(self.blankBtn_0,0)
        self.button_group.addButton(self.blankBtn_1,1)
        self.button_group.addButton(self.blankBtn_2,2)
        self.button_group.addButton(self.blankBtn_3,3)
        self.button_group.addButton(self.blankBtn_4,4)
        self.button_group.addButton(self.blankBtn_5,5)
        self.button_group.addButton(self.blankBtn_6,6)
        self.button_group.addButton(self.blankBtn_7,7)
        self.button_group.addButton(self.blankBtn_8,8)
        self.button_group.buttonClicked[int].connect(self.button)
        self.button_id=self.button_group.checkedId()
        
        #colours
        self.combo_box = QComboBox()
        self.combo_box.addItem('darkCyan')
        self.combo_box.addItem('white')
        self.combo_box.addItem('darkGrey')
        self.change_button = QPushButton('Change Color')
        self.change_button.clicked.connect(self.change_color)
        
        #Grid layout
        self.colour_box=QGridLayout()
        self.colour_box.addWidget(self.combo_box,0,0)
        self.colour_box.addWidget(self.change_button,0,1)
        self.colourbox=QWidget()
        self.colourbox.setLayout(self.colour_box)        
        layout.addWidget(self.server_label,0,3)
        layout.addWidget(self.line_edit,0,4)
        layout.addWidget(self.connectServer_button,0,5)
        layout.addWidget(self.blankBtn_0,1,0)
        layout.addWidget(self.blankBtn_1,1,1)
        layout.addWidget(self.blankBtn_2,1,2)
        layout.addWidget(self.blankBtn_3,2,0)
        layout.addWidget(self.blankBtn_4,2,1)
        layout.addWidget(self.blankBtn_5,2,2)
        layout.addWidget(self.blankBtn_6,3,0)
        layout.addWidget(self.blankBtn_7,3,1)
        layout.addWidget(self.blankBtn_8,3,2) 
        layout.addWidget(self.server_messages,1,3)
        layout.addWidget(self.shape_label,5,0)
        layout.addWidget(self.winner_label,4,3)
        layout.addWidget(self.shape_OX)
        layout.setSpacing(15)
        self.grid=QWidget()
        self.grid.setLayout(layout)
        home=QGridLayout()
        home.addWidget(self.welcom_label,1,3)
        home.addWidget(self.startgame_button,5,2,5,3)
        home.addWidget(self.front_text,0,3)
        HBOX=QWidget()
        HBOX.setLayout(home)
        self.startgame_button.clicked.connect(self.start_game)
        
        hbox_2=QHBoxLayout()
        hbox_2.addWidget(self.shape_OX)
        self.HBOX_2=QWidget()
        self.HBOX_2.setLayout(hbox_2)
        
        self.vbox=QVBoxLayout()
        self.vbox.addWidget(HBOX)
        self.setLayout(self.vbox)
        self.connectServer_button.clicked.connect(self.connect_server)
        self.PlayLoop.updating_signal.connect(self.handle_message)
        
        #Sets new game on board
    def new_game(self):
        self.close()
        self.PlayLoop.exit()
        self.Widget_2=OXO_GAME()
        self.Widget_2.show()
        
        
        
        #Start new game
    def start_game(self):
        self.PlayLoop.host=self.line_edit.displayText()
        self.resize(600,350)
        self.vbox.addWidget(self.grid)
        self.vbox.addWidget(self.HBOX_2)
        self.vbox.addWidget(self.colourbox)
        self.vbox.addWidget(self.buttonG_layout)
        
        #closes GUI
    def Quit(self):
        self.close()
        
        #Changes colour of the GUI
    def change_color(self):
        self.colour_selected=self.combo_box.currentText()
        if self.colour_selected=="darkCyan":
            self.setStyleSheet('background-color: darkCyan') 
        if self.colour_selected=="white":
            self.setStyleSheet('background-color: white')      

        if self.colour_selected=="darkGrey":
            self.setStyleSheet('background-color: darkGrey')     
                      
        #Connects to server
    def connect_server(self):
        self.PlayLoop.host=self.line_edit.displayText()
        self.PlayLoop.start()
        self.vbox.addWidget(self.grid)
        self.vbox.addWidget(self.HBOX_2)
        self.vbox.addWidget(self.colourbox)
        self.vbox.addWidget(self.buttonG_layout)
        
        #Handles messages from the server
    def handle_message(self,msg):
        self.server_messages.setText(msg)
        if msg=='new game,O':
            s='new game,O'
            self.O_symbol=QPixmap('nought.gif')
            self.shape_OX.setPixmap(self.O_symbol)
        elif msg=='new game,X':
          
            s='new game,X'
            self.X_symbol=QPixmap('cross.gif')
            self.shape_OX.setPixmap(self.X_symbol)
         
         #Sets button pressed to player's character   
        if msg=='valid move,O,0':
            self.blankBtn_0.setStyleSheet("border-image:url(nought.gif)")
        elif msg=='valid move,X,0':
            self.blankBtn_0.setStyleSheet("border-image:url(cross.gif)")
        elif msg=='valid move,O,1':
            self.blankBtn_1.setStyleSheet("border-image:url(nought.gif)")
        elif msg=='valid move,X,1':
            self.blankBtn_1.setStyleSheet("border-image:url(cross.gif)")
        elif msg=='valid move,O,2':
            self.blankBtn_2.setStyleSheet("border-image:url(nought.gif)")
        elif msg=='valid move,X,2':
            self.blankBtn_2.setStyleSheet("border-image:url(cross.gif)")
        elif msg=='valid move,O,3':
            self.blankBtn_3.setStyleSheet("border-image:url(nought.gif)")
        elif msg=='valid move,X,3':
            self.blankBtn_3.setStyleSheet("border-image:url(cross.gif)") 
        elif msg=='valid move,O,4':
            self.blankBtn_4.setStyleSheet("border-image:url(nought.gif)")
        elif msg=='valid move,X,4':
            self.blankBtn_4.setStyleSheet("border-image:url(cross.gif)") 
        elif msg=='valid move,O,5':
            self.blankBtn_5.setStyleSheet("border-image:url(nought.gif)")
        elif msg=='valid move,X,5':
            self.blankBtn_5.setStyleSheet("border-image:url(cross.gif)")
        elif msg=='valid move,O,6':
            self.blankBtn_6.setStyleSheet("border-image:url(nought.gif)")
        elif msg=='valid move,X,6':
            self.blankBtn_6.setStyleSheet("border-image:url(cross.gif)")
        elif msg=='valid move,O,7':
            self.blankBtn_7.setStyleSheet("border-image:url(nought.gif)")
        elif msg=='valid move,X,7':
            self.blankBtn_7.setStyleSheet("border-image:url(cross.gif)")
        elif msg=='valid move,O,8':
            self.blankBtn_8.setStyleSheet("border-image:url(nought.gif)")
        elif msg=='valid move,X,8':
            self.blankBtn_8.setStyleSheet("border-image:url(cross.gif)") 
            
            #Display's winner
        elif msg=='game over,O':
            self.winner_label.setText("Player O won!")
            self.winner_label.setFont(QFont("Courier",10,3))
                  
        elif msg=='game over,X':
            self.winner_label.setText("Player X won!")
            self.winner_label.setFont(QFont("Courier",20,3))
            
        elif msg=='game over,T':
            self.winner_label.setText("It's a Tie!")
            self.winner_label.setFont(QFont("Courier",20,3))            
        
    def button(self,Id):
         
        message=str(Id)
        self.PlayLoop.making_moves(message)
        
def main():
    app = QApplication(sys.argv)
    game=OXO_GAME()
    game.show()
    sys.exit(app.exec_())
 
 
if __name__ == '__main__':
    main()


            
        
           
    def exit_clicked(self):     #closes window when close button is clicked
        self.close()    
         
        
        
def main():
    app = QApplication(sys.argv)
    my_widget = OXOWidget() # create MyWidget object
    my_widget.show()          # shows window
    sys.exit(app.exec_())      

main()