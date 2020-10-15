numbers = []
n = int(input())

for i in range(n):
    n_numbers = int(input())
    numbers.append(n_numbers)


print(float(sum(numbers)/len(numbers)))
