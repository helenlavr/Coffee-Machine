class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9
    cash = 550

    def __init__(self, action):
        self.action = action

    def state(self):
        while self.action != 'exit':
            if self.action == 'remaining':
                self.action = self.action
        # states: 'choosing an action'  'choosing a type of coffee' 'filling the coffee machine'
        # user input --> program determines how to interpret the line using the information about the current state.
        # after processing: state of coffee machine can be changed, or can stay the same.


coffee_machine = CoffeeMachine(input())
