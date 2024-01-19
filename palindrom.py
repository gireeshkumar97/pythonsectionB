a=int(input('enter a number'))
out=[]
for a in range(100,500):
    if str(a) == str(a)[::-1]:
        out+=[a]
print(out)
    