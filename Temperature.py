choice=input('Enter your choice[c to f or f to c]')
if choice=='c to f':
    C=float(input('enter celsius value= '))
    F=C*(9/5)+32
    print('The temp in fahrenheit:',F)
elif choice=='f to c':
    F=float(input('Enter Fahrenheit value= '))
    C=(F-32)*(5/9)
    print('The temp in fahrenheit:',C)
else:
    print('Enter value in Either celsius or fahrenheit only')
