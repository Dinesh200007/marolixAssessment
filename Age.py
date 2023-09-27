Age=int(input("Enter your Age= "))
if (Age<18):
    print("You are a Minor")
elif Age in range(18,65):
    print ('You are an Adult')
elif Age>=65:
    print('You are a Senior citizen')
else:
    print('Invalid input')
