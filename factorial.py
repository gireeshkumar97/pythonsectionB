#out=[i**2 if i%2==0 else i**3 for i in range (1,21)]
#print(out)
a={'a':'abc',1:1234,'b':'bcde',2:2345}
out={a[k]:k for k in a if isinstance(k,str)}