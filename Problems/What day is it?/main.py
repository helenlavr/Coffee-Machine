time_point = int(input())
utc = 0

if utc + 13 >= time_point >= utc - 10:
    print('Tuesday')
elif time_point >= utc + 14:
    print('Wednesday')
elif time_point <= utc - 11:
    print('Monday')
