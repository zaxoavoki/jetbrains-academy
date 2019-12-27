from coffee_machine import CoffeeMachine


def main():
    coffee_machine = CoffeeMachine()
    while True:
        if coffee_machine.state == 'waiting':
            command = input('Write action (buy, fill, take, remaining, exit): ')
            if command == 'exit':
                break
        elif coffee_machine.state == 'choosing_coffee':
            command = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        elif coffee_machine.state == 'filling_water':
            command = input('Write how many ml of water do you want to add: ')
        elif coffee_machine.state == 'filling_milk':
            command = input('Write how many ml of milk do you want to add: ')
        elif coffee_machine.state == 'filling_beans':
            command = input('Write how many grams of coffee beans do you want to add: ')
        elif coffee_machine.state == 'filling_cups':
            command = input('Write how many disposable cups of coffee do you want to add: ')

        coffee_machine.run_command(command)


if __name__ == '__main__':
    main()
