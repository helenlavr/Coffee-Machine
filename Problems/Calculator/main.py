import math
first_number = float(input())
second_number = float(input())
action = input()

if action == '+':
    print(first_number + second_number)
elif action == '-':
    print(first_number - second_number)
elif action == 'pow':
    print(math.pow(first_number, second_number))
elif action == '*':
    print(first_number * second_number)
elif second_number == 0:
    print('Division by 0!')
elif action == '/':
    print(first_number / second_number)
elif action == 'mod':
    print(first_number % second_number)
elif action == 'div':
    print(first_number // second_number)
