#### src/game-draft.py ####
## AI generated code for a Tic-Tac-Toe game model in a single file. (MVC pattern)

from enum import Enum
from typing import List, Tuple

class Turn(Enum):
    O = "O"
    X = "X"


class GameState(Enum):
    ONGOING = "Ongoing"
    WIN = "Win"
    DRAW = "Draw"


class SquareState(Enum):
    EMPTY = ""  # empty square
    O = "O"
    X = "X"


class Game:
    """
    Tic-Tac-Toe game model in a single file.
    - 3x3 board of SquareState
    - turn: whose turn it is (Turn.O or Turn.X)
    - steps: number of moves played
    - game_state: current GameState
    - winning_positions: list of winning triplets of coordinates
    """

    def __init__(self) -> None:
        # initialize winning positions (each as a tuple of three (row,col) pairs)
        self.winning_positions: List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]] = [
            # rows
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            # columns
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            # diagonals
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
        ]
        self.turn: Turn = Turn.X
        self.reset()

    def reset(self) -> None:
        """Reset game to initial state."""
        self.game_state: GameState = GameState.ONGOING
        self.steps: int = 0
        # 3x3 matrix filled with SquareState.M
        self.square_states: List[List[SquareState]] = [
            [SquareState.EMPTY for _ in range(3)] for _ in range(3)
        ]

    # Getters
    def get_turn(self) -> Turn:
        return self.turn

    def get_game_state(self) -> GameState:
        return self.game_state

    def get_square_states(self) -> List[List[SquareState]]:
        return self.square_states

    def get_square_state(self, i: int, j: int) -> SquareState:
        return self.square_states[i][j]

    def get_winning_positions(self):
        return self.winning_positions

    # Game logic / setters
    def update_square_state(self, i: int, j: int) -> bool:
        """
        Attempt to place the current turn mark at (i, j).
        Returns True if the move was successful, False otherwise (invalid move or game finished).
        After a successful move, update_game_state() is called and turn is flipped if game continues.
        """
        # basic bounds check
        if not (0 <= i < 3 and 0 <= j < 3):
            return False
        # can't play on occupied square or if game already finished
        if self.square_states[i][j] != SquareState.EMPTY:
            return False
        if self.game_state != GameState.ONGOING:
            return False

        # place mark
        self.square_states[i][j] = SquareState.O if self.turn == Turn.O else SquareState.X

        # update game state (increments steps and checks win/draw)
        self.update_game_state()

        # if game still ongoing, flip turn
        if self.game_state == GameState.ONGOING:
            self.flip_turn()

        return True

    def update_game_state(self) -> GameState:
        """
        Increment steps and determine if the game is a win, draw, or continues.
        Returns the new game state.
        """
        self.steps += 1

        # check all winning positions
        for triple in self.winning_positions:
            a, b, c = triple
            sa = self.square_states[a[0]][a[1]]
            sb = self.square_states[b[0]][b[1]]
            sc = self.square_states[c[0]][c[1]]
            if sa == sb == sc and sa != SquareState.EMPTY:
                self.game_state = GameState.WIN
                return self.game_state

        # if no winner and board full -> draw
        if self.steps >= 9:
            self.game_state = GameState.DRAW
            return self.game_state

        # otherwise game continues
        self.game_state = GameState.ONGOING
        return self.game_state

    def flip_turn(self) -> None:
        self.turn = Turn.X if self.turn == Turn.O else Turn.O