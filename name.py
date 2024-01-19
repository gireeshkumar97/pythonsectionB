a="Hello my name is abhi"
i=0
out= " "
while i<len(a):
    if a[i]=='Hello my name is abhi':
        out+=' '
else:
    out+=a[i]
    i+=1
    print(out)