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
class Square_State(Enum):
    EMPTY = 'Empty'
    O = 'O'
    X = 'X'

class Game:
    ## Reset logic:
    def reset(self):
        self.game_state = Game_State.ONGOING
        self.square_states = [[Square_State.EMPTY for _ in range(3)] for _ in range(3)]
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
    def get_square_states(self):
        return self.square_states
    
    def get_square_state(self, i, j):
        return self.square_states[i][j]
    
    def update_square_state(self, i, j):
        self.square_states[i][j] = Square_State[self.get_turn().value]
    
def testing():
    game = Game()
    squares = game.get_square_states()
    for row in squares: print([row[i].value for i in range(len(row))])
    while 1:
        i = int(input("i: "))
        j = int(input("j: "))
        if i == j == 9: break
        if i < 0 or j < 0 or i >= 3 or j >= 3: continue
        game.update_square_state(i, j)

        for row in squares: print([row[i].value for i in range(len(row))])

    for row in squares: print([type(row[i]) for i in range(len(row))])
# testing()