import pickle


class Game:
    def __init__(self, name, board):
        self.save_name = name
        self.save_board = board

    def get_board(self):
        return self.save_board


