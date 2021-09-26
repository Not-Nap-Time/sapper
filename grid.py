import random
import pickle
import cell
from game_board import GameBoard
from game import Game
from utils import check_pos, save_level


def load_level(name):
    try:
        with open(name + '.pkl', 'rb') as data:
            return pickle.load(data)
    except Exception:
        print('Такого файла не существует!\n')
        return load_level(input("Введите новый путь\n"))


def load_board(game):
    board = game.get_board()
    board.print_board()
    flag = True
    while flag and not board.is_win():
        x = int(input("Введите координаты клетки по x\n"))
        y = int(input("Введите координаты клетки по y\n"))
        action = str(input("Введите действие(open or flag)\n"))
        if (((action != 'open') and (action != 'flag')) or (x <= 0) or
                (y <= 0) or (x > board.row) or (y > board.column)):
            print("Неверные данные")
            continue
        else:
            board.step(x - 1, y - 1, action)
            if not board.check_step(x - 1, y - 1):
                flag = False
            board.print_board()

    if not flag:
        print("Вы проиграли!")
        board.print_true_board()
    else:
        board.is_win()
        print("Вы победили!")
        board.print_true_board()


def new_game():
    row = int(input("Введите количество строк\n"))
    column = int(input("Введите количество столбцов\n"))
    bombs = int(input("Введите количетсов бомб\n"))
    board = GameBoard(bombs, column, row)
    board.print_board()
    flag = True
    save = False
    while flag and not board.is_win() and not save:
        x = int(input("Введите координаты клетки по x\n"))
        y = int(input("Введите координаты клетки по y\n"))
        action = str(input("Введите действие(open or flag or save)\n"))
        if (((action != 'open') and (action != 'flag') and (action != 'save')) or (x <= 0) or
                (y <= 0) or (x > row) or (y > column)):
            print("Неверные данные")
            continue
        elif action == "save":
            break
        else:
            board.step(x - 1, y - 1, action)
            if not board.check_step(x - 1, y - 1):
                flag = False
            board.print_board()

    if not flag:
        print("Вы проиграли!")
        board.print_true_board()
    elif board.is_win():
        print("Вы победили!")
        board.print_true_board()
    else:
        name = input("Введите имя сохранения\n")
        game = Game(name, board)
        save_level(game)


def start_game():
    game_mode = int(input("Начать новую игру - 1, загрузить существующую - 0\n"))
    if game_mode:
        new_game()
    else:
        name = input("Введите название файла:\n")
        load_board(load_level(name))


if __name__ == "__main__":
    start_game()




