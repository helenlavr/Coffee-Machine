#  recommended A
# too much B
# sleep H

# a <= b

def sleep(a, b, h):
    if h < a:
        print('Deficiency')
    elif h > b:
        print('Excess')
    elif a <= h <= b:
        print('Normal')


sleep(int(input()), int(input()), int(input()))
