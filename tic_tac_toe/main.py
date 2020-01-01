from tic_tac_toe import TicTacToe


def main():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.print_field()

    while True:
        input_ = input('Enter the coordinates: ').split()
        if tic_tac_toe.check_input(input_):
            if tic_tac_toe.move():
                tic_tac_toe.print_field()
                if tic_tac_toe.check_win():
                    break


if __name__ == '__main__':
    main()
