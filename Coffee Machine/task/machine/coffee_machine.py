money = 550
water = 400
milk = 540
coffee_beans = 120
cups = 9


def coffee_machine_status():
    print(f'\nThe coffee machine has:\n{water} of water\n{milk} of milk\n{coffee_beans} of coffee beans\n{cups} disposable cups\n${money} of money')


def coffee_machine_making(water1, milk1, coffee_beans1, money1):
    global money, water, milk, coffee_beans, cups
    water -= water1
    milk -= milk1
    coffee_beans -= coffee_beans1
    money += money1
    cups -= 1


# (water, milk, coffee beans, cost)

def espresso():
    global water, coffee_beans
    if water < 250:
        print('Sorry, not enough water!')
    elif coffee_beans < 16:
        print('Sorry, not enough coffee beans!')
    else:
        print('I have enough resources, making you a coffee!')
        coffee_machine_making(250, 0,  16, 4)


def latte():
    global water, milk, coffee_beans
    if water < 350:
        print('Sorry, not enough water!')
    elif milk < 75:
        print('Sorry, not enough milk!')
    elif coffee_beans < 20:
        print('Sorry, not enough coffee beans!')
    else:
        print('I have enough resources, making you a coffee!')
        coffee_machine_making(350, 75, 20, 7)


def cappuccino():
    global water, milk, coffee_beans
    if water < 200:
        print('Sorry, not enough water!')
    elif milk < 100:
        print('Sorry, not enough milk!')
    elif coffee_beans < 12:
        print('Sorry, not enough coffee beans!')
    else:
        print('I have enough resources, making you a coffee!')
        coffee_machine_making(200, 100, 12, 6)


def choices():
    while True:
        action = input('\nWrite action (buy, fill, take, remaining, exit): ')
        if action == 'fill':
            replenished()
        elif action == 'take':
            withdraw()
        elif action == 'buy':
            buy = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
            if buy == '1':
                espresso()
            elif buy == '2':
                latte()
            elif buy == '3':
                cappuccino()
        elif action == 'remaining':
            coffee_machine_status()
        elif action == 'exit':
            break


def replenished():
    global water, milk, coffee_beans, cups
    water += int(input('\nWrite how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    coffee_beans += int(input('Write how many grams of coffee beans do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee do you want to add: '))


def withdraw():
    global money
    print(f'I gave you ${money}')
    money -= money


def main():
    choices()


main()
