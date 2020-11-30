import random

class Dice:
    def __init__(self):
        self.score = 0
    
    def roll(self):
        self.score = random.randint(1,6)
        print(f"Dice Roll: {self.score}")
        return self.score