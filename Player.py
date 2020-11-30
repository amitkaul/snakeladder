import Board
import Dice

class Player:
    Player_State = {"TO_PLAY":"Welcome to game. Keep trying!", 
                    "PLAYING": "Hope you are enjoying! Keep pushing.", 
                    "WON":"Congratulations on your win!"}
                    
    
    def __init__(self, name,board, score=0):
        self.state = "TO_PLAY"
        self.name = name
        self.score = score
        self.board = board
        self.maxScore = board.getBoardSize()
    
    def getPlayerInfo(self):
        print(f" Hi {self.name} ! Your score is {self.score}. {self.Player_State[self.state]} \n ")

    def updateScore(self,score):
        print(f"Updating Score from {self.score} to {score}")
        self.score = score
        self.getPlayerInfo()

    def updateState(self,state):
        self.state = state
    def getState(self):
        return self.state

    
    def playStartGame(self, dice_roll):
        if(dice_roll == 6):
            self.updateState("PLAYING") #playing
            self.updateScore(1) # Hop to first square
        else:
            self.getPlayerInfo()


    def playNextStop(self,dice_roll):
        
        newScore = self.score + dice_roll

        if (newScore > self.maxScore ):
            print(f" Almost There! Try {self.maxScore - self.score} dice roll ")
            return

        if(newScore == self.maxScore):
            self.updateState("WON") # won
            self.updateScore(newScore)
            return

        finalScore = self.board.checkSnakeOrLadder(newScore)
        
        self.updateScore(finalScore)
        
        

    def play(self):

        dice = Dice.Dice()
        dice_roll = dice.roll()
        keepPlaying  = True

        if (self.state == "TO_PLAY"):
            self.playStartGame(dice_roll)

        elif (self.state == "PLAYING"):
            self.playNextStop(dice_roll)

        elif (self.state == "WON"):
            keepPlaying = False
        
        return keepPlaying
        
        
