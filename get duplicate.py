st=('rohit sharma')
i=0
out=' '
res=''
for char in st:
    if char not in out:
        out+=char
    else:
        res+=char
print(res)

