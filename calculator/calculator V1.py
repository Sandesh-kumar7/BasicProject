def sum(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
       return ' cannot divide by zero'
    else:
       return a/b

while True:
 print('=========CALCULATOR========')
 print('1.addition')
 print('2.subtraction')
 print('3.multiplication')
 print('4.divide')
 print('5.exit')
 print()
 try:
  choice=int(input())
 except ValueError:
  print('Enter valid value')
  continue

 if choice==5:
    print('calculator close')
    break


 if choice in [1,2,3,4,]:
    try:
        a=int(input())
        b=int(input())

    except ValueError:
        print('Enter valid value')
        continue

    if choice==1:
        x=sum(a,b)
        print(f'Answer is {x}')
    elif choice==2:
        x=subtraction(a,b)
        print(f'Answer is {x}')
    elif choice==3:
        x=multiply(a,b)
        print(f'Answer is {x}')
    elif choice==4:
        x=divide(a,b)
        print(f'Answer is {x}') 
         

 