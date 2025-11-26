#### src/game.py ####
#### Model file of Tic-Tac-Toe game (MVC pattern)

from enum import Enum 

class Turn(Enum):
    O = 'O'
    X = 'X'

class Game:
    def __init__(self):
        self.turn = Turn.X  # 'X' starts first    

    def get_turn(self):
        return self.turn
    
    def flip_turn(self):
        self.turn = Turn.O if self.turn == Turn.X else Turn.X