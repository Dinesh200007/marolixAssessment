Age=int(input('Enter your age= '))
if Age in range(0,13):
    print('Child')
elif Age in range(13,20):
    print('Teenager')
elif Age in range(20,60):
    print('Adult')
elif Age>=60:
    print('Senior Citizen')
else:
    print('Invalid input')