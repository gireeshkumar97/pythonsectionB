def toggle():
    a=input('enter a string')
    i=0
    b=''
    while len(a)>i:
        if'a'<=a[i]<='z':
            b+=chr(ord(a[i])-32)
        elif 'A'<=a[i]<='z':
            b+=chr(ord(ord.a[i])+32)
        else:
            b+=a[i]
        i+=1
    return b
print(toggle ())