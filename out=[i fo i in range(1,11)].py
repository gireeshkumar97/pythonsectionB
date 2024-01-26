def fact(num):
    out=1
    for i in range(1,num+1):
        out*=i
        return out
print([fact(i) for i in range (1,10)if i%2==0])
