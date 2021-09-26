import pickle


def check_pos(x, y, row, column):
    if x < 0 or x >= row or y < 0 or y >= column:
        return False
    else:
        return True


def save_level(game):
    with open(game.save_name + '.pkl', 'wb') as data:
        pickle.dump(game, data)
