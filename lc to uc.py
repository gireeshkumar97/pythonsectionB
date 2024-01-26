def toggle():
    a=(input('enter a string:-'))
    i=0
    out=''
    for i in a :
        if 'a'<=1<='z':
            out+=chr(ord(i)-32)
        elif 'A'<=i<='z':
            out+=chr(ord(i)+32)
        else:
            out+=i
    return out
print (toggle())