class CoffeeMachine:
    """
    Coffee Machine Project

    Learning outcomes:
    This project allows you to get a taste of Python.
    Practice working with functions, challenge yourself with l
    oops and conditions, and get more confident in Python.

    https://hyperskill.org/projects/68?goal=391
    """

    # Initial properties
    money = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9
    state = 'waiting'

    # Take money from the machine
    def take(self):
        print('I gave you ${}'.format(self.money))
        self.money = 0

    # Check if machine has enough resources
    def check_resources(self, water, milk, beans):
        if self.water < water:
            print('Sorry, not enough water!')
        if self.milk < milk:
            print('Sorry, not enough milk!')
        if self.beans < beans:
            print('Sorry, not enough coffee beans!')
        if self.cups < 1:
            print('Sorry, not enough disposable cups!')

    # Take needful resources and make coffee
    def make_coffee(self, water, milk, beans, money):
        self.check_resources(water, milk, beans)
        if self.water >= water and self.milk >= milk and self.beans >= beans and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= 1
            self.money += money

    # Choose which coffee user want
    def buy(self, code):
        if code == 1:
            self.make_coffee(250, 0, 16, 4)
        elif code == 2:
            self.make_coffee(350, 75, 20, 7)
        elif code == 3:
            self.make_coffee(200, 100, 12, 6)

    # Fill machine with new resources
    def fill(self, water=0, milk=0, beans=0, cups=0):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    # Check for different states and commands
    def run_command(self, command):
        if 'filling' not in self.state and 'choosing' not in self.state:
            print()

        if self.state == 'choosing_coffee':
            if command == 'back':
                self.state = 'waiting'
            else:
                self.buy(int(command))
            self.state = 'waiting'

        if self.state == 'filling_water':
            self.fill(water=int(command))
            self.state = 'filling_milk'
        elif self.state == 'filling_milk':
            self.fill(milk=int(command))
            self.state = 'filling_beans'
        elif self.state == 'filling_beans':
            self.fill(beans=int(command))
            self.state = 'filling_cups'
        elif self.state == 'filling_cups':
            self.fill(cups=int(command))
            self.state = 'waiting'

        if command == 'buy':
            self.state = 'choosing_coffee'

        if command == 'fill':
            self.state = 'filling_water'

        if command == 'take':
            self.take()

        if command == 'remaining':
            print(self)

        if 'filling' not in self.state:
            print()

        return True

    def __str__(self):
        return "The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of " \
               "money".format(self.water, self.milk, self.beans, self.cups, self.money)