a=input('enter a number 1:-')
b=input('enter a number 2:-')
c=input('enter a operator:-')

match c:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '%':
        print(a%b)
    case _:
        print('plese give a proper operator')