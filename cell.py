class Cell:

    def __init__(self, x, y, value):
        self._x = x
        self._y = y
        self._value = value
        if self._value == 'b':
            self._isBomb = True
        else:
            self._isBomb = False
        self.isOpen = False
        self.isFlag = False

    def set_flag(self):
        if not self.isFlag:
            self.isFlag = True
        else:
            self.isFlag = False

    def check_cell(self):
        return self.isOpen

    def check_bomb(self):
        return self._isBomb

    def open_cell(self) -> bool:
        if not self._isBomb and not self.isFlag and not self.isOpen:
            self.isOpen = True
            return True
        if self._isBomb and not self.isFlag and not self.isOpen:
            self.isOpen = True
            return False

    def view_cell(self):
        if self.isOpen:
            return self._value
        elif self.isFlag:
            return 'F'
        else:
            return '*'

    def view_cell_lose(self):
        return self._value

