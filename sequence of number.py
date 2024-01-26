def Range (m1,m2,m3):
    out=[]
    while m1<m2:
        out+=[m1 ]
        m1+=m3
    print(out)
Range(1,100,10)