print("""1.calculating Area
2.calculating perimeter
3.Exit""")
menu=int(input('Select option for calculating[1or2or3]= '))
if menu==1:
    l=int(input('enter length of rectangle= '))
    b=int(input('enter breadth of rectangle= '))
    Area=l*b
    print('Area of rectangle=',Area)
elif menu==2:
    l=int(input('enter length of rectangle= '))
    b=int(input('enter breadth of rectangle= '))
    perimeter=2*(l+b)
    print('perimeter of rectangle=',perimeter)
elif menu==3:
    print('Exit')
else:
    print('Invalid input')