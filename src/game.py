#### src/game.py ####
#### Model file of Tic-Tac-Toe game (MVC pattern)

from enum import Enum 

class Turn(Enum):
    O = 'O'
    X = 'X'
class Game_State(Enum):
    ONGOING = 'Ongoing'
    DRAW = 'Draw'
    WIN = 'Win'

class Game:
    ## Constructor to reset the game
    def __init__(self):
        self.turn = Turn.X  # 'X' starts first
        self.game_state = Game_State.ONGOING

    ## Turns:
    def get_turn(self):
        return self.turn
    
    def flip_turn(self):
        self.turn = Turn.O if self.turn == Turn.X else Turn.X

    ## Game State:
    def get_game_state(self):
        return self.game_state
    