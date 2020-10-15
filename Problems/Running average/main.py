numbers = [int(i) for i in input()]    # converting each input to int in a list

# average = []
# for i in range(len(numbers) - 1):
#     a = (numbers[i] + numbers[i + 1]) / 2
#     average.append(a)
#
# print(average)

# can get the whole for loop in one line with list comprehension
print([(numbers[i] + numbers[i + 1]) / 2 for i in range(len(numbers) - 1)])

# can also use enumerate
# print([(numbers[index] + numbers[index+1]) / 2 for (index, value) in enumerate(numbers) if value < len(numbers)])
