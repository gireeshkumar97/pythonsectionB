def prime(num):
    flag=True
    if isinstance(num,int) and num>1:
        for i in range (2,num):
            if num%i==0:
                flag=True
                break
        if flag:
            print(' primenumber')
        else:
            print('not aprime number')
prime(89)


        
