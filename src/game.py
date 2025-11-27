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
    ## Reset logic:
    def reset(self):
        self.game_state = Game_State.ONGOING
    def __init__(self):
        self.turn = Turn.X  # 'X' starts first
        self.reset()

    ## Turns logic:
    def get_turn(self):
        return self.turn
    
    def flip_turn(self):
        self.turn = Turn.O if self.turn == Turn.X else Turn.X

    ## Game State logic:
    def get_game_state(self):
        return self.game_state
    
    def update_game_state(self):
        return
    
    ## Square State logic: