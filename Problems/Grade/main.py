student_score = int(input())
maximum_score = int(input())

score_percentage = (student_score / maximum_score) * 100
if score_percentage < 60:
    print('F')
elif score_percentage < 70:
    print('D')
elif score_percentage < 80:
    print('C')
elif score_percentage < 90:
    print('B')
else:
    print('A')
