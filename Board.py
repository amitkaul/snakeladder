import json

class Board:
    def __init__(self):
        with open('board.json') as fh:
            conf = json.load(fh)
        self.snakes = conf['board']['snakes']
        self.ladders = conf['board']['ladders']
        self.size = int(conf['board']['size'])



    def __checkSnake(self,score):
        for head, tail in self.snakes.items():
            if (int(head) == score):
                print(f"God!! SNAKE at {score}")  
                return int(tail)
        return score

    def __checkLadder(self,score):
        for head, tail in self.ladders.items():
            if (int(head) == score):
                print(f" Yah!! LADDER at {score}")
                return int(tail)
        return score

    def getBoardSize(self):
        return self.size

    def checkSnakeOrLadder(self,score):

        final_score = self.__checkSnake(score)
        if (final_score != score):
            return final_score
        
        final_score = self.__checkLadder(score) 
        if (final_score != score):  
            return final_score
        return score
