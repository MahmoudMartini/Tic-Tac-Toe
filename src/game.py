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
        self.winning_positions = []
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
    
    def get_winning_positions(self):
        return self.winning_positions
    
    def update_game_state(self):
        # Check DRAW state:

        # Check WIN state:
        mat = self.square_states
        row = [False]*3
        col = [False]*3
        diag = [False]*2
        for i in range(3):
            row[i] = (mat[i][0] == mat[i][1] == mat[i][2] != Square_State.EMPTY)
            col[i] = (mat[0][i] == mat[1][i] == mat[2][i] != Square_State.EMPTY)
        diag[0] = (mat[0][0] == mat[1][1] == mat[2][2] != Square_State.EMPTY)
        diag[1] = (mat[0][2] == mat[1][1] == mat[2][0] != Square_State.EMPTY)

        indeces = []
        for i in range(3):
            if row[i]: indeces += [(i, 0), (i, 1), (i, 2)]
            if col[i]: indeces += [(0, i), (1, i), (2, i)]
        if diag[0]: indeces += [(0, 0), (1, 1), (2, 2)]
        if diag[1]: indeces += [(0, 2), (1, 1), (2, 0)]
        
        if indeces:
            self.game_state = Game_State.WIN
            self.winning_positions = indeces
        # Else: ONGOING
        
        return (col, row, diag)
    
    ## Square State logic:
    def get_square_states(self):
        return self.square_states
    
    def get_square_state(self, i, j):
        return self.square_states[i][j]
    
    def update_square_state(self, i, j):
        self.square_states[i][j] = Square_State[self.get_turn().value]
    
def testing_square_states():
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
def testing_game_states():
    game = Game()
    squares = game.get_square_states()
    for row in squares: print([row[i].value for i in range(len(row))])
    while 1:
        i = int(input("i: "))
        j = int(input("j: "))
        if i == j == 9: break
        if i < 0 or j < 0 or i >= 3 or j >= 3: continue
        game.update_square_state(i, j)
        print(game.update_game_state())

        for row in squares: print([row[i].value for i in range(len(row))])
        print(game.get_game_state())
        print(game.get_winning_positions())

# testing_game_states()

# """ 
# 0 1 
# 1 2
# 1 1 
# 2 1 
# """