class TicTacToe:
    """
    Everybody knows this game from childhood. This is the game, where the price
    of a mistake is too high: it usually costs you the game. You can become a
    real master of this game by mastering only one possible option, so it also
    teaches you that simple is always better than complex. What’s the game? Yes,
    this is Tic-Tac-Toe, also known as noughts and crosses or Xs and Os. It’s
    meant to be a paper game, but we are programmers, so why not make a game by
    ourselves? Let’s get started!
    """

    field = ['_'] * 9
    position = []
    turn = 'X'

    def print_field(self):
        print('---------')
        print('| {} {} {} |'.format(self.field[0], self.field[1], self.field[2]))
        print('| {} {} {} |'.format(self.field[3], self.field[4], self.field[5]))
        print('| {} {} {} |'.format(self.field[6], self.field[7], self.field[8]))
        print('---------')

    def check_win(self):
        to_test = [self.field[:3], self.field[3:6], self.field[6:], self.field[::3], self.field[1::3], self.field[2::3],
                   self.field[::4], self.field[2:8:2]]
        tested = [test[0] for test in to_test if test in (list('XXX'), list('OOO'))]
        if tested.count('X') > 0 and tested.count('O') > 0 or abs(self.field.count('X') - self.field.count('O')) >= 2:
            print('Impossible')
            return True
        elif tested.count('X') > 0:
            print('X wins')
            return True
        elif tested.count('O') > 0:
            print('O wins')
            return True
        elif self.field.count('_') == 0:
            print('Draw')
            return True
        return False

    def check_input(self, input_):
        if len(input_) == 2 and input_[0].isdigit() and input_[1].isdigit():
            if 1 <= int(input_[0]) <= 3 and 1 <= int(input_[1]) <= 3:
                self.position = [int(input_[0]), int(input_[1])]
                return True
            else:
                print('Coordinates should be from 1 to 3!')
                return False
        print('You should enter numbers!')
        return False

    def move(self):
        if self.field[6 - ((self.position[1] - 1) * 3) + (self.position[0] - 1)] == '_':
            self.field[6 - ((self.position[1] - 1) * 3) + (self.position[0] - 1)] = self.turn
            self.turn = 'O' if self.turn == 'X' else 'X'
            return True
        print('This cell is occupied! Choose another one!')
        return False
