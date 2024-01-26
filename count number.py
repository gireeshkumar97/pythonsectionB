def print(num):
    flag=True
    if isinstance(num,int)and num>1:
        for i in range (2,num):
            if num%i==0:
                flag=True
                break
            if flag:
                print('not a primenumber')
            else:
                print('prime number')
        else:
            print('invalid')
        
