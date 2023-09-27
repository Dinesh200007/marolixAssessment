marks=int(input('Enter Exam score= '))
if marks in range(90,101):
    print('Grade A')
elif marks in range(80,90):
    print('Grade B')
elif marks in range(70,80):
    print('Grade C')
elif marks in range(60,70):
    print('Grade D')
elif marks<60:
    print('Fail F')
else:
    print ('Not attended for exam')

