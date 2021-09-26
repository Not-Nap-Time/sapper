import random
from cell import Cell
from utils import check_pos

class GameBoard:
    def __init__(self, bombs, column, row):
        self.bombs = bombs
        self.column = column
        self.row = row
        self._board = self.cell_matrix(self.bomb_counter(self.generate_random_board(self.bombs, self.column, self.row)))
        self.opened_cells = 0

    def get_board(self):
        return self._board

    def check_step(self, x, y):
        if self._board[x][y].check_cell() and self._board[x][y].check_bomb():
            return False
        else:
            return True

    def step(self, x, y, action):
        if action == "flag":
            self._board[x][y].set_flag()

        if action == "open":
            if not self._board[x][y].check_cell():
                self._board[x][y].open_cell()
                self.opened_cells += 1
            if self._board[x][y].view_cell() == 0:
                if check_pos(x + 1, y + 1, len(self._board), len(self._board[0])) and \
                        not self._board[x+1][y+1].check_cell():
                    self.step(x+1, y+1, "open")

                if check_pos(x, y + 1, len(self._board), len(self._board[0])) and \
                        not self._board[x][y+1].check_cell():
                    self.step(x, y + 1, "open")

                if check_pos(x + 1, y, len(self._board), len(self._board[0])) and \
                        not self._board[x+1][y].check_cell():
                    self.step(x + 1, y, "open")

                if check_pos(x - 1, y + 1, len(self._board), len(self._board[0])) and \
                        not self._board[x-1][y+1].check_cell():
                    self.step(x - 1, y + 1, "open")

                if check_pos(x + 1, y - 1, len(self._board), len(self._board[0])) and \
                        not self._board[x+1][y-1].check_cell():
                    self.step(x + 1, y - 1, "open")

                if check_pos(x, y - 1, len(self._board), len(self._board[0])) and \
                        not self._board[x][y-1].check_cell():
                    self.step(x, y - 1, "open")

                if check_pos(x-1, y, len(self._board), len(self._board[0])) and \
                        not self._board[x-1][y].check_cell():
                    self.step(x-1, y, "open")

                if check_pos(x-1, y - 1, len(self._board), len(self._board[0])) and \
                        not self._board[x-1][y-1].check_cell():
                    self.step(x-1, y - 1, "open")

    def print_board(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                print(self._board[i][j].view_cell(), end=' ')
            print()

    def is_win(self):
        if self.column*self.row - self.opened_cells == self.bombs:
            return True
        else:
            return False

    def print_true_board(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                print(self._board[i][j].view_cell_lose(), end=' ')
            print()


    def cell_matrix(self, board):

        list_of_cell = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = Cell(i, j, board[i][j])
                list_of_cell.append(cell)

        matrix = []

        for i in range(len(board)):
            matrix.append(list_of_cell[len(board[0]) * i:(len(board[0]) * i + len(board[0]))])

        return matrix

    def bomb_counter(self, board):
        time_board = []  # подсчет бомб с помощью костыля
        for i in range(len(board) + 2):
            time_board.append([0] * (len(board[0]) + 2))
        for i in range(len(board) + 2):
            for j in range(len(board[0]) + 2):
                if ((i != 0) and (j != 0) and
                (j != len(board[0]) + 1) and (i != len(board) + 1)):
                    time_board[i][j] = board[i-1][j-1]

        for i in range(len(time_board)):
            for j in range(len(time_board[i])):
                if time_board[i][j] == 'b':
                    if time_board[i + 1][j + 1] != 'b':
                        time_board[i + 1][j + 1] += 1

                    if time_board[i][j + 1] != 'b':
                        time_board[i][j + 1] += 1

                    if time_board[i + 1][j] != 'b':
                        time_board[i + 1][j] += 1

                    if time_board[i - 1][j + 1] != 'b':
                        time_board[i - 1][j + 1] += 1

                    if time_board[i + 1][j - 1] != 'b':
                        time_board[i + 1][j - 1] += 1

                    if time_board[i][j - 1] != 'b':
                        time_board[i][j - 1] += 1

                    if time_board[i - 1][j] != 'b':
                        time_board[i - 1][j] += 1

                    if time_board[i - 1][j - 1] != 'b':
                        time_board[i - 1][j - 1] += 1
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = time_board[i + 1][j + 1]

        return board


    def generate_random_board(self, bombs, column, row):
        list_for_shuffle = []
        for i in range(column * row):
            if bombs > 0:
                list_for_shuffle.append('b')  # Заполнение бомбами
                bombs -= 1
            else:
                list_for_shuffle.append(0)
        random.shuffle(list_for_shuffle)

        board = []
        for i in range(row):
            board.append(list_for_shuffle[column * i:(column * i + column)])  # делаем двумерный массив, где только бомбы

        return board

