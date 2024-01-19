import random
number=random.randint(100,1000000)
while True:
    a=int(input('Enter a number'))
    if a==number:
        print('congrats! you succesfully guessed the number',a)
        break
    elif a<number:
        print('enter a some grater number')
    else:
        print('enter a some lesser number')