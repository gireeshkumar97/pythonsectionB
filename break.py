a=input('gireesh kumar:-')
i=-1
while i>=-len(a):
    if a[i]not in a[:i-1]:
        print(a[i])
        break
    i-=1
 
