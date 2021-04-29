



# Connect 4 is a game where opponents take turns
# dropping red or black discs into a 7 x 6 vertically
# suspended grid.
#
# The game ends either when one player creates a line
# of four consecutive discs of their color (horizontally,
# vertically, or diagonally), or when there are no more
# spots left in the grid.

#Design and implement Connect 4.
import unittest

MAX_ROWS = 6
MAX_COLS = 7
SYMBOLS = ' XO'

class GameStatus:
    def __init__(self, winner, nextplayer, isdraw):
        self.winner = winner
        self.isdraw = isdraw
        self.nextplayer = nextplayer

    def __str__(self):
        if self.winner:
            return "Winner is " + self.winner
        if self.isdraw:
            return "It'd a draw"
        return "Next player is " + self.nextplayer

    def IsGameOver(self):
        if self.isdraw or self.winner:
            return True
        return False

    def SwitchPlayer(self):
        next = SYMBOLS[2] if self.nextplayer == SYMBOLS[1] else SYMBOLS[1]
        return GameStatus(self.winner, next, self.isdraw)

class ConnectFour:
    def __init__(self):
        self.board = [[SYMBOLS[0]] * MAX_ROWS for _ in range(MAX_COLS)]
        self.state = GameStatus(None, SYMBOLS[1], False)


    def PlayAtColumn(self, column):
        if self.state.IsGameOver():
            raise Exception("Game over", self.state)
        c = self.board[column]
        if c[-1] != SYMBOLS[0]:
            raise Exception('Column is full', column, c)
        row = 0
        while c[row] != SYMBOLS[0]:
            row += 1
        c[row] = self.state.nextplayer
        won = self.CheckWinner(column, row)
        self.winner = self.state.nextplayer
        if won:
            self.state = GameStatus(self.state.nextplayer, None, False)
        elif self.NoMorePlays():
            self.state = GameStatus(None, None, True)
        else:
            self.state = self.state.SwitchPlayer()
        return self.state

    def CheckWinner(self, column, row):
        return self.CheckVertical(column, row) \
            or self.CheckDiagonal(column, row, -1) \
            or self.CheckDiagonal(column, row, 1) \
            or self.CheckHorizontal(column, row)

    def CheckVertical(self, column, row):
        m = self.board[column][row]
        for i in range(1, 4):
            if i > row or self.board[column][row - i] != m:
                return False
        return True

    def CheckDiagonal(self, column, row, dx):
        m = self.board[column][row]
        for i in range(1, 4):
            if i > row or column+i*dx < 0 \
                    or column+i*dx >= MAX_COLS \
                    or self.board[column+i*dx][row - i] != m:
                return False
        return True

    def CheckHorizontal(self, column, row):
        m = self.board[column][row]
        while column > 0 and self.board[column - 1][row] == m:
            column -= 1
        count = 1
        while column < MAX_COLS - 1 and self.board[column + 1][row] == m:
            column += 1
            count += 1
        return count >= 4

    def NoMorePlays(self):
        for c in self.board:
            if c[-1] == SYMBOLS[0]:
                return False
        return True


class TestDaily733(unittest.TestCase):

    def test_base(self):
        b = ConnectFour()
        r = b.PlayAtColumn(3)
        self.assertIsNone(r.winner)
        self.assertEqual(r.nextplayer, 'O')
        self.assertEqual(r.isdraw, False)

    def test_cross_win_across(self):
        b = ConnectFour()
        r = b.PlayAtColumn(0)
        r = b.PlayAtColumn(0)
        r = b.PlayAtColumn(1)
        r = b.PlayAtColumn(1)
        r = b.PlayAtColumn(2)
        r = b.PlayAtColumn(2)
        r = b.PlayAtColumn(3)
        self.assertEqual(r.winner, 'X')
        self.assertIsNone(r.nextplayer)
        self.assertEqual(r.isdraw, False)

    def test_naught_win_vertical(self):
        b = ConnectFour()
        r = b.PlayAtColumn(2)
        r = b.PlayAtColumn(2)
        r = b.PlayAtColumn(3)
        r = b.PlayAtColumn(2)
        r = b.PlayAtColumn(3)
        r = b.PlayAtColumn(2)
        r = b.PlayAtColumn(3)
        self.assertIsNone(r.winner)
        self.assertEqual(r.nextplayer, 'O')
        self.assertEqual(r.isdraw, False)
        r = b.PlayAtColumn(2)
        self.assertEqual(r.winner, 'O')
        self.assertIsNone(r.nextplayer)
        self.assertEqual(r.isdraw, False)

