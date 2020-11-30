import Player
import Board

class SL_Game:
    
    Game_State = {"START": "Welcome to Snake and Ladders" , 
                  "IN_PROGRESS": "Hope You are enjoying!" , 
                  "END": "Thanks for playing. Please come back!"}


    def __init__(self):
        self.players = []
        self.board = Board.Board()
        self.state = ""
        self.num_players = 0


    def printGameState(self):
        print(f"{SL_Game.Game_State[self.state]}")
    
    def updateGameState(self, state):
        self.state = state
        self.printGameState()
    
    def inputNumOfPlayers(self):
        self.num_players = int(input("How many players are playing today? : "))

    def onboardPlayers(self):
        self.updateGameState("START")
        self.inputNumOfPlayers()
        for i in range(0, self.num_players):
            name = input(f" Please enter {i+1} Player Name: ")
            new_player = Player.Player(name, self.board)
            self.players.append(new_player)
        self.updateGameState("IN_PROGRESS")

    def playGame(self):
        round = 1
        while(self.state != "END"):
            print(f"Round {round} =>")
            input("Press ENTER to continue ...")
            print("\n")
            for i in range(0, self.num_players):
                self.players[i].play()
                if (self.players[i].getState() == "WON"):
                    self.updateGameState("END")
                    break
            round += 1



